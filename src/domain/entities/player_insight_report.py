from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID


@dataclass(slots=True, frozen=True)
class PlayerInsightReport:
    """AI-assisted contextualization layer. Derived artifact, not authoritative analytical truth."""

    id: UUID
    player_id: UUID
    analysis_id: UUID
    created_at: datetime

    summary: str | None = field(default=None)
    key_observations: list[str] | None = field(default=None)
    recommended_focus: list[str] | None = field(default=None)
    limitations: list[str] | None = field(default=None)
    ai_model_used: str | None = field(default=None)

    def __post_init__(self) -> None:
        if self.summary is not None and not self.summary.strip():
            raise ValueError("summary must not be whitespace-only.")

        if self.ai_model_used is not None and not self.ai_model_used.strip():
            raise ValueError("ai_model_used must not be whitespace-only.")

        _LIST_FIELDS = ("key_observations", "recommended_focus", "limitations")
        for field_name in _LIST_FIELDS:
            entries = getattr(self, field_name)
            if entries is not None:
                for entry in entries:
                    if not entry or not entry.strip():
                        raise ValueError(
                            f"{field_name} entries must not be empty or whitespace-only."
                        )
