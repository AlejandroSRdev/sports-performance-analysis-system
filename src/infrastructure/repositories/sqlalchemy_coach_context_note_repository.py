from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.coach_context_note import CoachContextNote
from src.infrastructure.database.mappers import coach_context_note_mapper
from src.infrastructure.database.models.coach_context_note_model import CoachContextNoteModel


class SQLAlchemyCoachContextNoteRepository:

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, note: CoachContextNote) -> None:
        model = coach_context_note_mapper.to_model(note)
        self._session.merge(model)

    def list_by_player_id(self, player_id: UUID) -> list[CoachContextNote]:
        stmt = (
            select(CoachContextNoteModel)
            .where(CoachContextNoteModel.player_id == player_id)
            .order_by(CoachContextNoteModel.created_at.asc())
        )
        models = self._session.execute(stmt).scalars().all()
        return [coach_context_note_mapper.to_domain(m) for m in models]
