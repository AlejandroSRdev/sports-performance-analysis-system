from typing import Protocol
from uuid import UUID

from src.domain.entities.player_performance_analysis import PlayerPerformanceAnalysis


class PlayerPerformanceAnalysisRepository(Protocol):

    def save(self, analysis: PlayerPerformanceAnalysis) -> None: ...

    def get_by_id(self, analysis_id: UUID) -> PlayerPerformanceAnalysis | None: ...

    def list_by_player_id(self, player_id: UUID) -> list[PlayerPerformanceAnalysis]: ...

    def get_latest_by_player_id(self, player_id: UUID) -> PlayerPerformanceAnalysis | None: ...
