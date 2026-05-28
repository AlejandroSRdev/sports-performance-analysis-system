from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class ImportFederationStatsRequestDTO:
    source_url: str
    snapshot_date: date
