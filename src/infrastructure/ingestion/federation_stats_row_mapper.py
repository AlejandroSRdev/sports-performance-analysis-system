from decimal import Decimal, InvalidOperation

from src.application.dto.federation_player_stats_row_dto import FederationPlayerStatsRowDTO
from src.infrastructure.ingestion.exceptions import FederationRowMappingError

_PLAYER_NAME_COLUMNS = ["player", "jugador", "nombre", "name"]
_TEAM_COLUMNS = ["team", "equipo", "club"]
_JERSEY_COLUMNS = ["#", "jersey", "dorsal", "num"]
_AGGREGATE_ROW_NAMES = frozenset({"totals", "total", "opponents", "oponentes"})


def _to_int(value: object) -> int | None:
    """Strict integer parser. Does not split composite strings."""
    if value is None:
        return None
    try:
        s = str(value).strip()
        if not s or s.lower() in ("nan", "-", ""):
            return None
        return int(float(s))
    except (ValueError, TypeError):
        return None


def _parse_games_played(value: object) -> int | None:
    """Parse gp-gs composite field. Extracts games_played (first component only)."""
    if value is None:
        return None
    s = str(value).strip()
    if not s or s.lower() == "nan":
        return None
    if "-" in s:
        s = s.split("-", 1)[0].strip()
    try:
        return int(float(s))
    except (ValueError, TypeError):
        return None


def _parse_sb_att(value: object) -> tuple[int | None, int | None]:
    """Parse sb-att composite field into (stolen_bases, caught_stealing).

    Format: 'sb-att' where caught_stealing = att - sb.
    Raises FederationRowMappingError if att < sb.
    """
    if value is None:
        return (None, None)
    s = str(value).strip()
    if not s or s.lower() == "nan":
        return (None, None)
    if "-" not in s:
        try:
            return (int(float(s)), None)
        except (ValueError, TypeError):
            return (None, None)
    parts = s.split("-", 1)
    try:
        sb = int(float(parts[0].strip()))
        att = int(float(parts[1].strip()))
    except (ValueError, TypeError):
        return (None, None)
    if att < sb:
        raise FederationRowMappingError(
            f"Invalid sb-att value: attempted steals ({att}) < stolen bases ({sb})."
        )
    return (sb, att - sb)


def _to_decimal(value: object) -> Decimal | None:
    if value is None:
        return None
    try:
        s = str(value).strip()
        if not s or s.lower() in ("nan", ""):
            return None
        return Decimal(s)
    except (InvalidOperation, ValueError, TypeError):
        return None


class FederationStatsRowMapper:

    def map_row(self, row: dict[str, object]) -> FederationPlayerStatsRowDTO:
        player_name = self._extract_player_name(row)
        if player_name is None:
            raise FederationRowMappingError("Row has no parseable player name.")
        if not any(c.isalpha() for c in player_name):
            raise FederationRowMappingError(f"Row is a decorative separator row: {player_name}")
        normalized_name = player_name.lower().strip()
        if normalized_name in _AGGREGATE_ROW_NAMES or "total" in normalized_name:
            raise FederationRowMappingError(f"Row is an aggregate row: {player_name}")

        team = self._extract_first(row, _TEAM_COLUMNS)
        jersey_number = self._extract_jersey(row)

        stolen_bases, caught_stealing = _parse_sb_att(
            row.get("sb-att") or row.get("sb")
        )

        return FederationPlayerStatsRowDTO(
            player_name=player_name,
            team=team,
            jersey_number=jersey_number,
            games_played=_parse_games_played(row.get("gp-gs") or row.get("gp")),
            at_bats=_to_int(row.get("ab")),
            runs=_to_int(row.get("r")),
            hits=_to_int(row.get("h")),
            doubles=_to_int(row.get("2b")),
            triples=_to_int(row.get("3b")),
            home_runs=_to_int(row.get("hr")),
            runs_batted_in=_to_int(row.get("rbi")),
            total_bases=_to_int(row.get("tb")),
            walks=_to_int(row.get("bb")),
            hit_by_pitch=_to_int(row.get("hbp")),
            strikeouts=_to_int(row.get("so")),
            grounded_into_double_play=_to_int(row.get("gdp")),
            sacrifice_flies=_to_int(row.get("sf")),
            sacrifice_hits=_to_int(row.get("sh")),
            stolen_bases=stolen_bases,
            caught_stealing=caught_stealing,
            batting_average=_to_decimal(row.get("avg")),
            on_base_percentage=_to_decimal(row.get("ob%")),
            slugging_percentage=_to_decimal(row.get("slg%")),
            putouts=_to_int(row.get("po")),
            assists=_to_int(row.get("a")),
            errors=_to_int(row.get("e")),
            fielding_percentage=_to_decimal(row.get("fld%")),
        )

    def _extract_player_name(self, row: dict[str, object]) -> str | None:
        for col in _PLAYER_NAME_COLUMNS:
            val = row.get(col)
            if val is not None:
                s = str(val).strip()
                if s and s.lower() != "nan":
                    return s
        return None

    def _extract_first(self, row: dict[str, object], candidates: list[str]) -> str | None:
        for col in candidates:
            val = row.get(col)
            if val is not None:
                s = str(val).strip()
                if s and s.lower() != "nan":
                    return s
        return None

    def _extract_jersey(self, row: dict[str, object]) -> int | None:
        for col in _JERSEY_COLUMNS:
            val = row.get(col)
            if val is not None:
                s = str(val).strip().lstrip("#")
                try:
                    return int(float(s))
                except (ValueError, TypeError):
                    continue
        return None
