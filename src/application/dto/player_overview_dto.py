from dataclasses import dataclass, field

from src.domain.entities.player import Player
from src.domain.entities.player_insight_report import PlayerInsightReport
from src.domain.entities.player_performance_analysis import PlayerPerformanceAnalysis
from src.domain.entities.player_statistics_snapshot import PlayerStatisticsSnapshot


@dataclass(slots=True)
class PlayerOverviewDTO:
    player: Player
    latest_snapshot: PlayerStatisticsSnapshot | None = field(default=None)
    latest_analysis: PlayerPerformanceAnalysis | None = field(default=None)
    latest_ai_report: PlayerInsightReport | None = field(default=None)
