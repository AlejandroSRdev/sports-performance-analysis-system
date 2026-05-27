from src.domain.entities.player_performance_analysis import PlayerPerformanceAnalysis
from src.infrastructure.database.models.player_performance_analysis_model import PlayerPerformanceAnalysisModel


def to_domain(model: PlayerPerformanceAnalysisModel) -> PlayerPerformanceAnalysis:
    return PlayerPerformanceAnalysis(
        id=model.id,
        player_id=model.player_id,
        analysis_period_start=model.analysis_period_start,
        analysis_period_end=model.analysis_period_end,
        created_at=model.created_at,
        batting_trend=model.batting_trend,
        discipline_trend=model.discipline_trend,
        contact_trend=model.contact_trend,
        fielding_trend=model.fielding_trend,
        overall_trend=model.overall_trend,
        priority_area=model.priority_area,
        consistency_score=model.consistency_score,
    )


def to_model(entity: PlayerPerformanceAnalysis) -> PlayerPerformanceAnalysisModel:
    model = PlayerPerformanceAnalysisModel()
    model.id = entity.id
    model.player_id = entity.player_id
    model.analysis_period_start = entity.analysis_period_start
    model.analysis_period_end = entity.analysis_period_end
    model.created_at = entity.created_at
    model.batting_trend = entity.batting_trend
    model.discipline_trend = entity.discipline_trend
    model.contact_trend = entity.contact_trend
    model.fielding_trend = entity.fielding_trend
    model.overall_trend = entity.overall_trend
    model.priority_area = entity.priority_area
    model.consistency_score = entity.consistency_score
    return model
