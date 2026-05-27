from pydantic import BaseModel, Field


class RegisterCoachContextRequestSchema(BaseModel):
    note: str = Field(..., min_length=1)
