from src.domain.entities.player_statistics_snapshot import PlayerStatisticsSnapshot
from src.infrastructure.database.models.player_statistics_snapshot_model import PlayerStatisticsSnapshotModel


def to_domain(model: PlayerStatisticsSnapshotModel) -> PlayerStatisticsSnapshot:
    return PlayerStatisticsSnapshot(
        id=model.id,
        player_id=model.player_id,
        snapshot_date=model.snapshot_date,
        created_at=model.created_at,
        source_url=model.source_url,
        games_played=model.games_played,
        at_bats=model.at_bats,
        runs=model.runs,
        hits=model.hits,
        doubles=model.doubles,
        triples=model.triples,
        home_runs=model.home_runs,
        runs_batted_in=model.runs_batted_in,
        walks=model.walks,
        strikeouts=model.strikeouts,
        stolen_bases=model.stolen_bases,
        batting_average=model.batting_average,
        on_base_percentage=model.on_base_percentage,
        slugging_percentage=model.slugging_percentage,
        putouts=model.putouts,
        assists=model.assists,
        errors=model.errors,
        fielding_percentage=model.fielding_percentage,
    )


def to_model(entity: PlayerStatisticsSnapshot) -> PlayerStatisticsSnapshotModel:
    model = PlayerStatisticsSnapshotModel()
    model.id = entity.id
    model.player_id = entity.player_id
    model.snapshot_date = entity.snapshot_date
    model.created_at = entity.created_at
    model.source_url = entity.source_url
    model.games_played = entity.games_played
    model.at_bats = entity.at_bats
    model.runs = entity.runs
    model.hits = entity.hits
    model.doubles = entity.doubles
    model.triples = entity.triples
    model.home_runs = entity.home_runs
    model.runs_batted_in = entity.runs_batted_in
    model.walks = entity.walks
    model.strikeouts = entity.strikeouts
    model.stolen_bases = entity.stolen_bases
    model.batting_average = entity.batting_average
    model.on_base_percentage = entity.on_base_percentage
    model.slugging_percentage = entity.slugging_percentage
    model.putouts = entity.putouts
    model.assists = entity.assists
    model.errors = entity.errors
    model.fielding_percentage = entity.fielding_percentage
    return model
