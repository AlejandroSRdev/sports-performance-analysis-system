import uuid
from datetime import datetime, timezone

from src.application.dto.register_coach_context_request_dto import RegisterCoachContextRequestDTO
from src.application.dto.register_coach_context_response_dto import RegisterCoachContextResponseDTO
from src.application.exceptions import PlayerNotFoundError
from src.domain.entities.coach_context_note import CoachContextNote
from src.domain.repositories.coach_context_note_repository import CoachContextNoteRepository
from src.domain.repositories.player_repository import PlayerRepository
from src.shared.logging import StructuredLogger


class RegisterCoachContextUseCase:

    def __init__(
        self,
        player_repository: PlayerRepository,
        coach_context_note_repository: CoachContextNoteRepository,
        logger: StructuredLogger,
    ) -> None:
        self._player_repository = player_repository
        self._coach_context_note_repository = coach_context_note_repository
        self._logger = logger

    def execute(self, request_dto: RegisterCoachContextRequestDTO) -> RegisterCoachContextResponseDTO:
        self._logger.info(
            "register_coach_context_started",
            player_id=str(request_dto.player_id),
        )

        try:
            player = self._player_repository.get_by_id(request_dto.player_id)
            if player is None:
                self._logger.warning(
                    "register_coach_context_player_not_found",
                    player_id=str(request_dto.player_id),
                )
                raise PlayerNotFoundError(request_dto.player_id)

            context_note = CoachContextNote(
                id=uuid.uuid4(),
                player_id=request_dto.player_id,
                note=request_dto.note,
                created_at=datetime.now(tz=timezone.utc),
            )

            self._coach_context_note_repository.save(context_note)

            self._logger.info(
                "coach_context_note_persisted",
                context_note_id=str(context_note.id),
                player_id=str(context_note.player_id),
            )

            self._logger.info(
                "register_coach_context_completed",
                context_note_id=str(context_note.id),
                player_id=str(context_note.player_id),
            )

            return RegisterCoachContextResponseDTO(
                context_note_id=context_note.id,
                player_id=context_note.player_id,
                created_at=context_note.created_at,
            )

        except PlayerNotFoundError:
            raise
        except Exception as exc:
            self._logger.error(
                "register_coach_context_failed",
                player_id=str(request_dto.player_id),
                error=str(exc),
            )
            raise
