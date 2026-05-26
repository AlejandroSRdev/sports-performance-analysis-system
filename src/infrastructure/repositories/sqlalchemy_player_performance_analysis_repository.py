from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.player_performance_analysis import PlayerPerformanceAnalysis
from src.infrastructure.database.mappers import player_performance_analysis_mapper
from src.infrastructure.database.models.player_performance_analysis_model import PlayerPerformanceAnalysisModel


class SQLAlchemyPlayerPerformanceAnalysisRepository:

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, analysis: PlayerPerformanceAnalysis) -> None:
        model = player_performance_analysis_mapper.to_model(analysis)
        self._session.merge(model)

    def get_by_id(self, analysis_id: UUID) -> PlayerPerformanceAnalysis | None:
        stmt = select(PlayerPerformanceAnalysisModel).where(
            PlayerPerformanceAnalysisModel.id == analysis_id
        )
        model = self._session.execute(stmt).scalar_one_or_none()
        if model is None:
            return None
        return player_performance_analysis_mapper.to_domain(model)

    def list_by_player_id(self, player_id: UUID) -> list[PlayerPerformanceAnalysis]:
        stmt = (
            select(PlayerPerformanceAnalysisModel)
            .where(PlayerPerformanceAnalysisModel.player_id == player_id)
            .order_by(PlayerPerformanceAnalysisModel.created_at.asc())
        )
        models = self._session.execute(stmt).scalars().all()
        return [player_performance_analysis_mapper.to_domain(m) for m in models]

    def get_latest_by_player_id(self, player_id: UUID) -> PlayerPerformanceAnalysis | None:
        stmt = (
            select(PlayerPerformanceAnalysisModel)
            .where(PlayerPerformanceAnalysisModel.player_id == player_id)
            .order_by(PlayerPerformanceAnalysisModel.created_at.desc())
            .limit(1)
        )
        model = self._session.execute(stmt).scalar_one_or_none()
        if model is None:
            return None
        return player_performance_analysis_mapper.to_domain(model)
