from typing import Protocol
from uuid import UUID

from src.domain.entities.player_insight_report import PlayerInsightReport


class PlayerInsightReportRepository(Protocol):

    def save(self, report: PlayerInsightReport) -> None: ...

    def get_by_analysis_id(self, analysis_id: UUID) -> PlayerInsightReport | None: ...

    def list_by_player_id(self, player_id: UUID) -> list[PlayerInsightReport]: ...
