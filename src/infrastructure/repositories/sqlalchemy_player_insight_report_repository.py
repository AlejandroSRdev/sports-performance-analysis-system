from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.player_insight_report import PlayerInsightReport
from src.infrastructure.database.mappers import player_insight_report_mapper
from src.infrastructure.database.models.player_insight_report_model import PlayerInsightReportModel


class SQLAlchemyPlayerInsightReportRepository:

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, report: PlayerInsightReport) -> None:
        model = player_insight_report_mapper.to_model(report)
        self._session.merge(model)

    def get_by_analysis_id(self, analysis_id: UUID) -> PlayerInsightReport | None:
        stmt = select(PlayerInsightReportModel).where(
            PlayerInsightReportModel.analysis_id == analysis_id
        )
        model = self._session.execute(stmt).scalar_one_or_none()
        if model is None:
            return None
        return player_insight_report_mapper.to_domain(model)

    def list_by_player_id(self, player_id: UUID) -> list[PlayerInsightReport]:
        stmt = (
            select(PlayerInsightReportModel)
            .where(PlayerInsightReportModel.player_id == player_id)
            .order_by(PlayerInsightReportModel.created_at.asc())
        )
        models = self._session.execute(stmt).scalars().all()
        return [player_insight_report_mapper.to_domain(m) for m in models]
