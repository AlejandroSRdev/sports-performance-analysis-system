from fastapi import Depends

from src.application.use_cases.import_federation_stats_use_case import ImportFederationStatsUseCase
from src.application.use_cases.register_coach_context_use_case import RegisterCoachContextUseCase
from src.infrastructure.ingestion.federation_html_client import FederationHtmlClient
from src.infrastructure.ingestion.federation_stats_row_mapper import FederationStatsRowMapper
from src.infrastructure.ingestion.overall_statistics_table_selector import OverallStatisticsTableSelector
from src.infrastructure.repositories.sqlalchemy_coach_context_note_repository import (
    SQLAlchemyCoachContextNoteRepository,
)
from src.infrastructure.repositories.sqlalchemy_player_repository import SQLAlchemyPlayerRepository
from src.infrastructure.repositories.sqlalchemy_player_statistics_snapshot_repository import (
    SQLAlchemyPlayerStatisticsSnapshotRepository,
)
from src.presentation.dependencies.repositories import (
    get_coach_context_note_repository,
    get_player_repository,
    get_player_statistics_snapshot_repository,
)
from src.shared.logging import get_logger


def get_import_federation_stats_use_case(
    player_repository: SQLAlchemyPlayerRepository = Depends(get_player_repository),
    snapshot_repository: SQLAlchemyPlayerStatisticsSnapshotRepository = Depends(
        get_player_statistics_snapshot_repository
    ),
) -> ImportFederationStatsUseCase:
    return ImportFederationStatsUseCase(
        html_client=FederationHtmlClient(),
        table_selector=OverallStatisticsTableSelector(),
        row_mapper=FederationStatsRowMapper(),
        player_repository=player_repository,
        snapshot_repository=snapshot_repository,
        logger=get_logger("import_federation_stats"),
    )


def get_register_coach_context_use_case(
    player_repository: SQLAlchemyPlayerRepository = Depends(get_player_repository),
    coach_context_note_repository: SQLAlchemyCoachContextNoteRepository = Depends(
        get_coach_context_note_repository
    ),
) -> RegisterCoachContextUseCase:
    return RegisterCoachContextUseCase(
        player_repository=player_repository,
        coach_context_note_repository=coach_context_note_repository,
        logger=get_logger("register_coach_context"),
    )
