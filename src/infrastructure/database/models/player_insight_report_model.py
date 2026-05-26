import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base


class PlayerInsightReportModel(Base):
    __tablename__ = "player_insight_reports"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    player_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("players.id", ondelete="RESTRICT"), nullable=False
    )
    analysis_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("player_performance_analyses.id", ondelete="RESTRICT"),
        nullable=False,
        unique=True,
    )
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    key_observations = mapped_column(ARRAY(Text), nullable=True)
    recommended_focus = mapped_column(ARRAY(Text), nullable=True)
    limitations = mapped_column(ARRAY(Text), nullable=True)
    ai_model_used: Mapped[str | None] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    player = relationship("PlayerModel", back_populates="insight_reports")
    analysis = relationship(
        "PlayerPerformanceAnalysisModel", back_populates="insight_report"
    )
