from datetime import date

from pydantic import BaseModel, Field


class ImportFederationStatsRequestSchema(BaseModel):
    source_url: str = Field(..., min_length=1)
    snapshot_date: date | None = Field(default=None)
