import uuid
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Index, Integer, Numeric, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base


class PlayerStatisticsSnapshotModel(Base):
    __tablename__ = "player_statistics_snapshots"
    __table_args__ = (
        UniqueConstraint("player_id", "snapshot_date", name="uq_player_snapshot_date"),
        Index("ix_player_statistics_snapshots_player_id", "player_id"),
        Index("ix_player_statistics_snapshots_snapshot_date", "snapshot_date"),
    )

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    player_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("players.id", ondelete="RESTRICT"), nullable=False
    )
    snapshot_date: Mapped[date] = mapped_column(Date, nullable=False)
    source_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    # General
    games_played: Mapped[int | None] = mapped_column(Integer, nullable=True)
    at_bats: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # Batting counts
    runs: Mapped[int | None] = mapped_column(Integer, nullable=True)
    hits: Mapped[int | None] = mapped_column(Integer, nullable=True)
    doubles: Mapped[int | None] = mapped_column(Integer, nullable=True)
    triples: Mapped[int | None] = mapped_column(Integer, nullable=True)
    home_runs: Mapped[int | None] = mapped_column(Integer, nullable=True)
    runs_batted_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    total_bases: Mapped[int | None] = mapped_column(Integer, nullable=True)
    walks: Mapped[int | None] = mapped_column(Integer, nullable=True)
    hit_by_pitch: Mapped[int | None] = mapped_column(Integer, nullable=True)
    strikeouts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    grounded_into_double_play: Mapped[int | None] = mapped_column(Integer, nullable=True)
    sacrifice_flies: Mapped[int | None] = mapped_column(Integer, nullable=True)
    sacrifice_hits: Mapped[int | None] = mapped_column(Integer, nullable=True)
    stolen_bases: Mapped[int | None] = mapped_column(Integer, nullable=True)
    caught_stealing: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # Batting rates
    batting_average: Mapped[Decimal | None] = mapped_column(Numeric(5, 3), nullable=True)
    on_base_percentage: Mapped[Decimal | None] = mapped_column(Numeric(5, 3), nullable=True)
    slugging_percentage: Mapped[Decimal | None] = mapped_column(Numeric(5, 3), nullable=True)

    # Fielding
    putouts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    errors: Mapped[int | None] = mapped_column(Integer, nullable=True)
    fielding_percentage: Mapped[Decimal | None] = mapped_column(Numeric(5, 3), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    imported_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    player = relationship("PlayerModel", back_populates="statistics_snapshots")
