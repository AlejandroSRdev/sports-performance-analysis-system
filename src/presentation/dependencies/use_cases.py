from fastapi import Depends

from src.application.use_cases.register_coach_context_use_case import RegisterCoachContextUseCase
from src.infrastructure.repositories.sqlalchemy_coach_context_note_repository import (
    SQLAlchemyCoachContextNoteRepository,
)
from src.infrastructure.repositories.sqlalchemy_player_repository import SQLAlchemyPlayerRepository
from src.presentation.dependencies.repositories import (
    get_coach_context_note_repository,
    get_player_repository,
)
from src.shared.logging import get_logger


def get_register_coach_context_use_case(
    player_repository: SQLAlchemyPlayerRepository = Depends(get_player_repository),
    coach_context_note_repository: SQLAlchemyCoachContextNoteRepository = Depends(
        get_coach_context_note_repository
    ),
) -> RegisterCoachContextUseCase:
    return RegisterCoachContextUseCase(
        player_repository=player_repository,
        coach_context_note_repository=coach_context_note_repository,
        logger=get_logger("register_coach_context"),
    )
