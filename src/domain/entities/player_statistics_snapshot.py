from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID


@dataclass(slots=True, frozen=True)
class PlayerStatisticsSnapshot:
    """Immutable historical statistical truth for a player at a given point in time."""

    id: UUID
    player_id: UUID
    snapshot_date: date
    created_at: datetime

    # General
    games_played: int | None = field(default=None)
    at_bats: int | None = field(default=None)

    # Batting
    batting_average: Decimal | None = field(default=None)
    on_base_percentage: Decimal | None = field(default=None)
    slugging_percentage: Decimal | None = field(default=None)
    ops: Decimal | None = field(default=None)
    runs: int | None = field(default=None)
    hits: int | None = field(default=None)
    doubles: int | None = field(default=None)
    triples: int | None = field(default=None)
    home_runs: int | None = field(default=None)
    runs_batted_in: int | None = field(default=None)
    walks: int | None = field(default=None)
    strikeouts: int | None = field(default=None)
    stolen_bases: int | None = field(default=None)

    # Fielding
    fielding_percentage: Decimal | None = field(default=None)
    putouts: int | None = field(default=None)
    assists: int | None = field(default=None)
    errors: int | None = field(default=None)

    # Pitching
    earned_run_average: Decimal | None = field(default=None)
    innings_pitched: Decimal | None = field(default=None)
    wins: int | None = field(default=None)
    losses: int | None = field(default=None)
    earned_runs: int | None = field(default=None)
    pitching_strikeouts: int | None = field(default=None)
    walks_allowed: int | None = field(default=None)
    hits_allowed: int | None = field(default=None)

    # Per-game averages
    hits_per_game: Decimal | None = field(default=None)
    runs_per_game: Decimal | None = field(default=None)
    rbi_per_game: Decimal | None = field(default=None)
    strikeouts_per_game: Decimal | None = field(default=None)
    walks_per_game: Decimal | None = field(default=None)

    source_url: str | None = field(default=None)

    def __post_init__(self) -> None:
        _INT_FIELDS = (
            "games_played", "at_bats", "runs", "hits", "doubles", "triples",
            "home_runs", "runs_batted_in", "walks", "strikeouts", "stolen_bases",
            "putouts", "assists", "errors", "wins", "losses", "earned_runs",
            "pitching_strikeouts", "walks_allowed", "hits_allowed",
        )
        for field_name in _INT_FIELDS:
            value = getattr(self, field_name)
            if value is not None and value < 0:
                raise ValueError(f"{field_name} must be >= 0.")

        _DECIMAL_FIELDS = (
            "batting_average", "on_base_percentage", "slugging_percentage", "ops",
            "fielding_percentage", "earned_run_average", "innings_pitched",
            "hits_per_game", "runs_per_game", "rbi_per_game",
            "strikeouts_per_game", "walks_per_game",
        )
        for field_name in _DECIMAL_FIELDS:
            value = getattr(self, field_name)
            if value is not None and value < Decimal("0"):
                raise ValueError(f"{field_name} must be >= 0.")
