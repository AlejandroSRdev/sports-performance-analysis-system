from fastapi import Depends
from sqlalchemy.orm import Session

from src.infrastructure.repositories.sqlalchemy_coach_context_note_repository import (
    SQLAlchemyCoachContextNoteRepository,
)
from src.infrastructure.repositories.sqlalchemy_player_repository import SQLAlchemyPlayerRepository
from src.infrastructure.repositories.sqlalchemy_player_statistics_snapshot_repository import (
    SQLAlchemyPlayerStatisticsSnapshotRepository,
)
from src.presentation.dependencies.db import get_db


def get_player_repository(db: Session = Depends(get_db)) -> SQLAlchemyPlayerRepository:
    return SQLAlchemyPlayerRepository(db)


def get_coach_context_note_repository(
    db: Session = Depends(get_db),
) -> SQLAlchemyCoachContextNoteRepository:
    return SQLAlchemyCoachContextNoteRepository(db)


def get_player_statistics_snapshot_repository(
    db: Session = Depends(get_db),
) -> SQLAlchemyPlayerStatisticsSnapshotRepository:
    return SQLAlchemyPlayerStatisticsSnapshotRepository(db)
