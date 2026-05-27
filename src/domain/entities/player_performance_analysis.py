from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID


@dataclass(slots=True, frozen=True)
class PlayerPerformanceAnalysis:
    """Deterministic backend-generated analytical conclusion. Historical analytical artifact."""

    id: UUID
    player_id: UUID
    analysis_period_start: date
    analysis_period_end: date
    created_at: datetime

    batting_trend: str | None = field(default=None)
    discipline_trend: str | None = field(default=None)
    contact_trend: str | None = field(default=None)
    fielding_trend: str | None = field(default=None)
    overall_trend: str | None = field(default=None)

    priority_area: str | None = field(default=None)
    consistency_score: Decimal | None = field(default=None)

    def __post_init__(self) -> None:
        if self.analysis_period_start > self.analysis_period_end:
            raise ValueError(
                "analysis_period_start must be <= analysis_period_end."
            )

        if self.consistency_score is not None:
            if self.consistency_score < Decimal("0") or self.consistency_score > Decimal("1"):
                raise ValueError("consistency_score must be between 0 and 1.")

        _TREND_FIELDS = (
            "batting_trend", "discipline_trend", "contact_trend",
            "fielding_trend", "overall_trend",
        )
        for field_name in _TREND_FIELDS:
            value = getattr(self, field_name)
            if value is not None and not value.strip():
                raise ValueError(f"{field_name} must not be whitespace-only.")
