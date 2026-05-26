from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.application.dto.register_coach_context_request_dto import RegisterCoachContextRequestDTO
from src.application.exceptions import PlayerNotFoundError
from src.application.use_cases.register_coach_context_use_case import RegisterCoachContextUseCase
from src.presentation.dependencies.db import get_db
from src.presentation.dependencies.use_cases import get_register_coach_context_use_case
from src.presentation.schemas.register_coach_context_request import RegisterCoachContextRequestSchema
from src.presentation.schemas.register_coach_context_response import RegisterCoachContextResponseSchema

router = APIRouter()


@router.post(
    "/players/{player_id}/context-notes",
    response_model=RegisterCoachContextResponseSchema,
    status_code=201,
)
def register_coach_context(
    player_id: UUID,
    body: RegisterCoachContextRequestSchema,
    db: Session = Depends(get_db),
    use_case: RegisterCoachContextUseCase = Depends(get_register_coach_context_use_case),
):
    try:
        request_dto = RegisterCoachContextRequestDTO(
            player_id=player_id,
            note=body.note,
        )
        result = use_case.execute(request_dto)
        db.commit()
        return RegisterCoachContextResponseSchema(
            context_note_id=result.context_note_id,
            player_id=result.player_id,
            created_at=result.created_at,
        )
    except PlayerNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"error": "PLAYER_NOT_FOUND"},
        )
