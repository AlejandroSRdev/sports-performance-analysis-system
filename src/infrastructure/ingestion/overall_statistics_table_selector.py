import pandas as pd
from src.infrastructure.ingestion.exceptions import TableStructureNotSupportedError

# Minimum required columns (lowercase) to identify the Overall Statistics table.
_REQUIRED_COLUMNS = {"ab", "h", "avg", "rbi", "fld%"}

# Accepted player name column labels (lowercase).
_PLAYER_NAME_COLUMNS = {"player", "jugador", "nombre", "name"}


class OverallStatisticsTableSelector:

    def select(self, html: str) -> pd.DataFrame:
        try:
            tables = pd.read_html(html)
        except ValueError as exc:
            raise TableStructureNotSupportedError(
                f"No HTML tables found: {exc}"
            ) from exc

        for table in tables:
            normalized = {col.lower().strip() for col in table.columns}
            if _REQUIRED_COLUMNS.issubset(normalized) and bool(normalized & _PLAYER_NAME_COLUMNS):
                table.columns = [col.lower().strip() for col in table.columns]
                return table

        raise TableStructureNotSupportedError(
            "No table matching the Overall Statistics column signature was found."
        )
