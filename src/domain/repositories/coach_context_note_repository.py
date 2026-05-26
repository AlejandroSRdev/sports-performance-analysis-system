from typing import Protocol
from uuid import UUID

from src.domain.entities.coach_context_note import CoachContextNote


class CoachContextNoteRepository(Protocol):

    def save(self, note: CoachContextNote) -> None: ...

    def list_by_player_id(self, player_id: UUID) -> list[CoachContextNote]: ...
