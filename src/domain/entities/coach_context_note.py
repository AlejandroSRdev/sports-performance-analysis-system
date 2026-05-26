from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class CoachContextNote:
    """Human contextual interpretation and manually introduced operational context."""

    id: UUID
    player_id: UUID
    note: str
    created_at: datetime

    def __post_init__(self) -> None:
        if not self.note or not self.note.strip():
            raise ValueError("CoachContextNote note must not be empty or whitespace-only.")
