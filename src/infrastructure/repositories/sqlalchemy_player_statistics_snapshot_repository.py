from datetime import date
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.player_statistics_snapshot import PlayerStatisticsSnapshot
from src.infrastructure.database.mappers import player_statistics_snapshot_mapper
from src.infrastructure.database.models.player_statistics_snapshot_model import PlayerStatisticsSnapshotModel


class SQLAlchemyPlayerStatisticsSnapshotRepository:

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, snapshot: PlayerStatisticsSnapshot) -> None:
        model = player_statistics_snapshot_mapper.to_model(snapshot)
        self._session.merge(model)

    def list_by_player_id(self, player_id: UUID) -> list[PlayerStatisticsSnapshot]:
        stmt = (
            select(PlayerStatisticsSnapshotModel)
            .where(PlayerStatisticsSnapshotModel.player_id == player_id)
            .order_by(PlayerStatisticsSnapshotModel.snapshot_date.asc())
        )
        models = self._session.execute(stmt).scalars().all()
        return [player_statistics_snapshot_mapper.to_domain(m) for m in models]

    def list_between_dates(
        self,
        player_id: UUID,
        start_date: date,
        end_date: date,
    ) -> list[PlayerStatisticsSnapshot]:
        stmt = (
            select(PlayerStatisticsSnapshotModel)
            .where(PlayerStatisticsSnapshotModel.player_id == player_id)
            .where(PlayerStatisticsSnapshotModel.snapshot_date >= start_date)
            .where(PlayerStatisticsSnapshotModel.snapshot_date <= end_date)
            .order_by(PlayerStatisticsSnapshotModel.snapshot_date.asc())
        )
        models = self._session.execute(stmt).scalars().all()
        return [player_statistics_snapshot_mapper.to_domain(m) for m in models]

    def get_latest_by_player_id(self, player_id: UUID) -> PlayerStatisticsSnapshot | None:
        stmt = (
            select(PlayerStatisticsSnapshotModel)
            .where(PlayerStatisticsSnapshotModel.player_id == player_id)
            .order_by(PlayerStatisticsSnapshotModel.snapshot_date.desc())
            .limit(1)
        )
        model = self._session.execute(stmt).scalar_one_or_none()
        if model is None:
            return None
        return player_statistics_snapshot_mapper.to_domain(model)
