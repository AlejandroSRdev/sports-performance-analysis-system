from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(slots=True)
class FederationPlayerStatsRowDTO:
    player_name: str
    team: str | None = field(default=None)
    jersey_number: int | None = field(default=None)

    games_played: int | None = field(default=None)
    at_bats: int | None = field(default=None)
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

    batting_average: Decimal | None = field(default=None)
    on_base_percentage: Decimal | None = field(default=None)
    slugging_percentage: Decimal | None = field(default=None)

    putouts: int | None = field(default=None)
    assists: int | None = field(default=None)
    errors: int | None = field(default=None)
    fielding_percentage: Decimal | None = field(default=None)
