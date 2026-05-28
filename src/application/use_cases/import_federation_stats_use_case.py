import uuid
from datetime import datetime, timezone

from src.application.dto.federation_player_stats_row_dto import FederationPlayerStatsRowDTO
from src.application.dto.import_federation_stats_request_dto import ImportFederationStatsRequestDTO
from src.application.dto.import_federation_stats_result_dto import ImportFederationStatsResultDTO
from src.application.services.operational_identity_builder import OperationalIdentityBuilder
from src.domain.entities.player import Player
from src.domain.entities.player_statistics_snapshot import PlayerStatisticsSnapshot
from src.domain.repositories.player_repository import PlayerRepository
from src.domain.repositories.player_statistics_snapshot_repository import PlayerStatisticsSnapshotRepository
from src.infrastructure.ingestion.exceptions import FederationRowMappingError
from src.infrastructure.ingestion.federation_html_client import FederationHtmlClient
from src.infrastructure.ingestion.federation_stats_row_mapper import FederationStatsRowMapper
from src.infrastructure.ingestion.overall_statistics_table_selector import OverallStatisticsTableSelector
from src.shared.logging import StructuredLogger


class ImportFederationStatsUseCase:

    def __init__(
        self,
        html_client: FederationHtmlClient,
        table_selector: OverallStatisticsTableSelector,
        row_mapper: FederationStatsRowMapper,
        player_repository: PlayerRepository,
        snapshot_repository: PlayerStatisticsSnapshotRepository,
        logger: StructuredLogger,
    ) -> None:
        self._html_client = html_client
        self._table_selector = table_selector
        self._row_mapper = row_mapper
        self._player_repository = player_repository
        self._snapshot_repository = snapshot_repository
        self._logger = logger

    def execute(self, dto: ImportFederationStatsRequestDTO) -> ImportFederationStatsResultDTO:
        self._logger.info(
            "federation_import_started",
            source_url=dto.source_url,
            snapshot_date=str(dto.snapshot_date),
        )

        html = self._html_client.fetch(dto.source_url)
        df = self._table_selector.select(html)

        self._logger.info("overall_statistics_table_detected", row_count=len(df))

        created_players = 0
        reused_players = 0
        snapshots_created = 0
        snapshots_skipped = 0
        failed_rows = 0
        imported_at = datetime.now(tz=timezone.utc)

        for idx, row_series in df.iterrows():
            row_dict: dict[str, object] = row_series.to_dict()

            try:
                row_dto: FederationPlayerStatsRowDTO = self._row_mapper.map_row(row_dict)

                identity_key = OperationalIdentityBuilder.build(
                    name=row_dto.player_name,
                    jersey_number=row_dto.jersey_number,
                    team=row_dto.team,
                )

                player = self._player_repository.find_by_operational_identity_key(identity_key)

                if player is None:
                    now = datetime.now(tz=timezone.utc)
                    player = Player(
                        id=uuid.uuid4(),
                        name=row_dto.player_name,
                        active=True,
                        created_at=now,
                        updated_at=now,
                        operational_identity_key=identity_key,
                        team=row_dto.team,
                        jersey_number=row_dto.jersey_number,
                    )
                    self._player_repository.save(player)
                    self._logger.info(
                        "player_created",
                        player_id=str(player.id),
                        identity_key=identity_key,
                        player_name=row_dto.player_name,
                    )
                    created_players += 1
                else:
                    self._logger.info(
                        "player_reused",
                        player_id=str(player.id),
                        identity_key=identity_key,
                    )
                    reused_players += 1

                if self._snapshot_repository.exists_for_player_and_snapshot_date(
                    player.id, dto.snapshot_date
                ):
                    self._logger.info(
                        "snapshot_skipped",
                        player_id=str(player.id),
                        snapshot_date=str(dto.snapshot_date),
                    )
                    snapshots_skipped += 1
                    continue

                snapshot = PlayerStatisticsSnapshot(
                    id=uuid.uuid4(),
                    player_id=player.id,
                    snapshot_date=dto.snapshot_date,
                    created_at=datetime.now(tz=timezone.utc),
                    imported_at=imported_at,
                    source_url=dto.source_url,
                    games_played=row_dto.games_played,
                    at_bats=row_dto.at_bats,
                    runs=row_dto.runs,
                    hits=row_dto.hits,
                    doubles=row_dto.doubles,
                    triples=row_dto.triples,
                    home_runs=row_dto.home_runs,
                    runs_batted_in=row_dto.runs_batted_in,
                    total_bases=row_dto.total_bases,
                    walks=row_dto.walks,
                    hit_by_pitch=row_dto.hit_by_pitch,
                    strikeouts=row_dto.strikeouts,
                    grounded_into_double_play=row_dto.grounded_into_double_play,
                    sacrifice_flies=row_dto.sacrifice_flies,
                    sacrifice_hits=row_dto.sacrifice_hits,
                    stolen_bases=row_dto.stolen_bases,
                    caught_stealing=row_dto.caught_stealing,
                    batting_average=row_dto.batting_average,
                    on_base_percentage=row_dto.on_base_percentage,
                    slugging_percentage=row_dto.slugging_percentage,
                    putouts=row_dto.putouts,
                    assists=row_dto.assists,
                    errors=row_dto.errors,
                    fielding_percentage=row_dto.fielding_percentage,
                )
                self._snapshot_repository.save(snapshot)
                self._logger.info(
                    "snapshot_created",
                    snapshot_id=str(snapshot.id),
                    player_id=str(player.id),
                    snapshot_date=str(dto.snapshot_date),
                )
                snapshots_created += 1

            except FederationRowMappingError as exc:
                self._logger.warning(
                    "federation_row_mapping_failed",
                    row_index=str(idx),
                    reason=str(exc),
                )
                failed_rows += 1
            except Exception as exc:
                self._logger.warning(
                    "federation_row_processing_failed",
                    row_index=str(idx),
                    reason=str(exc),
                )
                failed_rows += 1

        self._logger.info(
            "federation_import_completed",
            created_players=created_players,
            reused_players=reused_players,
            snapshots_created=snapshots_created,
            snapshots_skipped=snapshots_skipped,
            failed_rows=failed_rows,
        )

        return ImportFederationStatsResultDTO(
            imported_players=created_players + reused_players,
            created_players=created_players,
            reused_players=reused_players,
            snapshots_created=snapshots_created,
            snapshots_skipped=snapshots_skipped,
            failed_rows=failed_rows,
            source_url=dto.source_url,
            imported_at=imported_at,
        )
