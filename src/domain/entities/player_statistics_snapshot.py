from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID


@dataclass(slots=True, frozen=True)
class PlayerStatisticsSnapshot:
    """Immutable aggregated statistical state extracted from the federative Overall Statistics table."""

    id: UUID
    player_id: UUID
    snapshot_date: date
    created_at: datetime

    # General
    games_played: int | None = field(default=None)
    at_bats: int | None = field(default=None)

    # Batting counts
    runs: int | None = field(default=None)
    hits: int | None = field(default=None)
    doubles: int | None = field(default=None)
    triples: int | None = field(default=None)
    home_runs: int | None = field(default=None)
    runs_batted_in: int | None = field(default=None)
    total_bases: int | None = field(default=None)
    walks: int | None = field(default=None)
    hit_by_pitch: int | None = field(default=None)
    strikeouts: int | None = field(default=None)
    grounded_into_double_play: int | None = field(default=None)
    sacrifice_flies: int | None = field(default=None)
    sacrifice_hits: int | None = field(default=None)
    stolen_bases: int | None = field(default=None)
    caught_stealing: int | None = field(default=None)

    # Batting rates
    batting_average: Decimal | None = field(default=None)
    on_base_percentage: Decimal | None = field(default=None)
    slugging_percentage: Decimal | None = field(default=None)

    # Fielding
    putouts: int | None = field(default=None)
    assists: int | None = field(default=None)
    errors: int | None = field(default=None)
    fielding_percentage: Decimal | None = field(default=None)

    imported_at: datetime | None = field(default=None)
    source_url: str | None = field(default=None)

    def __post_init__(self) -> None:
        _INT_FIELDS = (
            "games_played", "at_bats", "runs", "hits", "doubles", "triples",
            "home_runs", "runs_batted_in", "total_bases", "walks", "hit_by_pitch",
            "strikeouts", "grounded_into_double_play", "sacrifice_flies", "sacrifice_hits",
            "stolen_bases", "caught_stealing", "putouts", "assists", "errors",
        )
        for field_name in _INT_FIELDS:
            value = getattr(self, field_name)
            if value is not None and value < 0:
                raise ValueError(f"{field_name} must be >= 0.")

        _DECIMAL_FIELDS = (
            "batting_average", "on_base_percentage", "slugging_percentage",
            "fielding_percentage",
        )
        for field_name in _DECIMAL_FIELDS:
            value = getattr(self, field_name)
            if value is not None and value < Decimal("0"):
                raise ValueError(f"{field_name} must be >= 0.")
