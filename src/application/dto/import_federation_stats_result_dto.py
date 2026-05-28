from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ImportFederationStatsResultDTO:
    imported_players: int
    created_players: int
    reused_players: int
    snapshots_created: int
    snapshots_skipped: int
    failed_rows: int
    source_url: str
    imported_at: datetime
