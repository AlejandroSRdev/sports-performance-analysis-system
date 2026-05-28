import pandas as pd
from src.infrastructure.ingestion.exceptions import TableStructureNotSupportedError

# Required columns (lowercase) that must all be present to identify the Overall Statistics table.
_REQUIRED_COLUMNS = {"ab", "h", "avg", "rbi", "fld%"}

# Accepted player name column labels (lowercase).
_PLAYER_NAME_COLUMNS = {"player", "jugador", "nombre", "name"}


def _normalize_header(value: object) -> str:
    return str(value).lower().strip()


class OverallStatisticsTableSelector:

    def select(self, html: str) -> pd.DataFrame:
        try:
            tables = pd.read_html(html)
        except ValueError as exc:
            raise TableStructureNotSupportedError(
                f"No HTML tables found: {exc}"
            ) from exc

        for table in tables:
            if table.empty or len(table) < 2:
                continue

            candidate_headers = [_normalize_header(v) for v in table.iloc[0]]
            header_set = set(candidate_headers)

            if _REQUIRED_COLUMNS.issubset(header_set) and bool(header_set & _PLAYER_NAME_COLUMNS):
                normalized_df = table.copy()
                normalized_df.columns = candidate_headers
                normalized_df = normalized_df.iloc[1:].reset_index(drop=True)
                return normalized_df

        raise TableStructureNotSupportedError(
            "No table matching the Overall Statistics column signature was found."
        )
