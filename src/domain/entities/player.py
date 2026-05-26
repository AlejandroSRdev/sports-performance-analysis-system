from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class Player:
    """Longitudinal player identity and analytical continuity anchor."""

    id: UUID
    name: str
    active: bool
    created_at: datetime
    updated_at: datetime
    team: str | None = field(default=None)
    jersey_number: int | None = field(default=None)

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise ValueError("Player name must not be empty or whitespace-only.")
        if self.jersey_number is not None and self.jersey_number < 0:
            raise ValueError("Player jersey_number must be >= 0.")
