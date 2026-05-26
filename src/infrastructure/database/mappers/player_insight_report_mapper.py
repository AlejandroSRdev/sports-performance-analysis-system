from src.domain.entities.player_insight_report import PlayerInsightReport
from src.infrastructure.database.models.player_insight_report_model import PlayerInsightReportModel


def to_domain(model: PlayerInsightReportModel) -> PlayerInsightReport:
    return PlayerInsightReport(
        id=model.id,
        player_id=model.player_id,
        analysis_id=model.analysis_id,
        created_at=model.created_at,
        summary=model.summary,
        key_observations=list(model.key_observations) if model.key_observations is not None else None,
        recommended_focus=list(model.recommended_focus) if model.recommended_focus is not None else None,
        limitations=list(model.limitations) if model.limitations is not None else None,
        ai_model_used=model.ai_model_used,
    )


def to_model(entity: PlayerInsightReport) -> PlayerInsightReportModel:
    model = PlayerInsightReportModel()
    model.id = entity.id
    model.player_id = entity.player_id
    model.analysis_id = entity.analysis_id
    model.created_at = entity.created_at
    model.summary = entity.summary
    model.key_observations = list(entity.key_observations) if entity.key_observations is not None else None
    model.recommended_focus = list(entity.recommended_focus) if entity.recommended_focus is not None else None
    model.limitations = list(entity.limitations) if entity.limitations is not None else None
    model.ai_model_used = entity.ai_model_used
    return model
