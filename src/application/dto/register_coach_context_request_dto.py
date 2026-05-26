from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class RegisterCoachContextRequestDTO:
    player_id: UUID
    note: str
