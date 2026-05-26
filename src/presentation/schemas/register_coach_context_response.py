from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class RegisterCoachContextResponseSchema(BaseModel):
    context_note_id: UUID
    player_id: UUID
    created_at: datetime
