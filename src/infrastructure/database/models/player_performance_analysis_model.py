import uuid
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base


class PlayerPerformanceAnalysisModel(Base):
    __tablename__ = "player_performance_analyses"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    player_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("players.id", ondelete="RESTRICT"), nullable=False
    )
    analysis_period_start: Mapped[date] = mapped_column(Date, nullable=False)
    analysis_period_end: Mapped[date] = mapped_column(Date, nullable=False)

    # Trend classifications — VARCHAR(20), not database ENUMs
    batting_trend: Mapped[str | None] = mapped_column(String(20), nullable=True)
    discipline_trend: Mapped[str | None] = mapped_column(String(20), nullable=True)
    contact_trend: Mapped[str | None] = mapped_column(String(20), nullable=True)
    fielding_trend: Mapped[str | None] = mapped_column(String(20), nullable=True)
    pitching_trend: Mapped[str | None] = mapped_column(String(20), nullable=True)
    overall_trend: Mapped[str | None] = mapped_column(String(20), nullable=True)

    priority_area: Mapped[str | None] = mapped_column(String(100), nullable=True)
    consistency_score: Mapped[Decimal | None] = mapped_column(Numeric(4, 3), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    player = relationship("PlayerModel", back_populates="performance_analyses")
    insight_report = relationship(
        "PlayerInsightReportModel", back_populates="analysis", uselist=False
    )
