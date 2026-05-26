from src.domain.entities.coach_context_note import CoachContextNote
from src.infrastructure.database.models.coach_context_note_model import CoachContextNoteModel


def to_domain(model: CoachContextNoteModel) -> CoachContextNote:
    return CoachContextNote(
        id=model.id,
        player_id=model.player_id,
        note=model.note,
        created_at=model.created_at,
    )


def to_model(entity: CoachContextNote) -> CoachContextNoteModel:
    model = CoachContextNoteModel()
    model.id = entity.id
    model.player_id = entity.player_id
    model.note = entity.note
    model.created_at = entity.created_at
    return model
