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
        batting_average=model.batting_average,
        on_base_percentage=model.on_base_percentage,
        slugging_percentage=model.slugging_percentage,
        ops=model.ops,
        runs=model.runs,
        hits=model.hits,
        doubles=model.doubles,
        triples=model.triples,
        home_runs=model.home_runs,
        runs_batted_in=model.runs_batted_in,
        walks=model.walks,
        strikeouts=model.strikeouts,
        stolen_bases=model.stolen_bases,
        fielding_percentage=model.fielding_percentage,
        putouts=model.putouts,
        assists=model.assists,
        errors=model.errors,
        earned_run_average=model.earned_run_average,
        innings_pitched=model.innings_pitched,
        wins=model.wins,
        losses=model.losses,
        earned_runs=model.earned_runs,
        pitching_strikeouts=model.pitching_strikeouts,
        walks_allowed=model.walks_allowed,
        hits_allowed=model.hits_allowed,
        hits_per_game=model.hits_per_game,
        runs_per_game=model.runs_per_game,
        rbi_per_game=model.rbi_per_game,
        strikeouts_per_game=model.strikeouts_per_game,
        walks_per_game=model.walks_per_game,
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
    model.batting_average = entity.batting_average
    model.on_base_percentage = entity.on_base_percentage
    model.slugging_percentage = entity.slugging_percentage
    model.ops = entity.ops
    model.runs = entity.runs
    model.hits = entity.hits
    model.doubles = entity.doubles
    model.triples = entity.triples
    model.home_runs = entity.home_runs
    model.runs_batted_in = entity.runs_batted_in
    model.walks = entity.walks
    model.strikeouts = entity.strikeouts
    model.stolen_bases = entity.stolen_bases
    model.fielding_percentage = entity.fielding_percentage
    model.putouts = entity.putouts
    model.assists = entity.assists
    model.errors = entity.errors
    model.earned_run_average = entity.earned_run_average
    model.innings_pitched = entity.innings_pitched
    model.wins = entity.wins
    model.losses = entity.losses
    model.earned_runs = entity.earned_runs
    model.pitching_strikeouts = entity.pitching_strikeouts
    model.walks_allowed = entity.walks_allowed
    model.hits_allowed = entity.hits_allowed
    model.hits_per_game = entity.hits_per_game
    model.runs_per_game = entity.runs_per_game
    model.rbi_per_game = entity.rbi_per_game
    model.strikeouts_per_game = entity.strikeouts_per_game
    model.walks_per_game = entity.walks_per_game
    return model
