import uuid
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base


class PlayerModel(Base):
    __tablename__ = "players"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    position: Mapped[str | None] = mapped_column(String(50), nullable=True)
    jersey_number: Mapped[int | None] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    statistics_snapshots = relationship(
        "PlayerStatisticsSnapshotModel", back_populates="player"
    )
    coach_context_notes = relationship(
        "CoachContextNoteModel", back_populates="player"
    )
    performance_analyses = relationship(
        "PlayerPerformanceAnalysisModel", back_populates="player"
    )
    insight_reports = relationship(
        "PlayerInsightReportModel", back_populates="player"
    )
