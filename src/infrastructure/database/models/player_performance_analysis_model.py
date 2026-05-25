import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, JSON, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base


class PlayerPerformanceAnalysisModel(Base):
    __tablename__ = "player_performance_analyses"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    player_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("players.id"), nullable=False
    )
    trend_classification: Mapped[str | None] = mapped_column(String(100), nullable=True)
    consistency_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    analysis_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    player = relationship("PlayerModel", back_populates="performance_analyses")
