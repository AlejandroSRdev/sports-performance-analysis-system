from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class RegisterCoachContextResponseDTO:
    context_note_id: UUID
    player_id: UUID
    created_at: datetime
