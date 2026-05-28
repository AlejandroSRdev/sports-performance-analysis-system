from datetime import date

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.application.dto.import_federation_stats_request_dto import ImportFederationStatsRequestDTO
from src.application.exceptions import ImportFederationStatsError, InvalidSourceUrlError
from src.application.use_cases.import_federation_stats_use_case import ImportFederationStatsUseCase
from src.infrastructure.ingestion.exceptions import (
    HtmlFetchFailedError,
    TableStructureNotSupportedError,
)
from src.presentation.dependencies.db import get_db
from src.presentation.dependencies.use_cases import get_import_federation_stats_use_case
from src.presentation.schemas.import_federation_stats_request import ImportFederationStatsRequestSchema
from src.presentation.schemas.import_federation_stats_response import ImportFederationStatsResponseSchema
from src.shared.logging import get_logger

router = APIRouter(tags=["imports"])
_logger = get_logger("import_routes")


@router.post(
    "/imports/federation-stats",
    response_model=ImportFederationStatsResponseSchema,
    status_code=201,
)
def import_federation_stats(
    body: ImportFederationStatsRequestSchema,
    db: Session = Depends(get_db),
    use_case: ImportFederationStatsUseCase = Depends(get_import_federation_stats_use_case),
):
    try:
        resolved_date = body.snapshot_date or date.today()
        request_dto = ImportFederationStatsRequestDTO(
            source_url=body.source_url,
            snapshot_date=resolved_date,
        )
        result = use_case.execute(request_dto)
        db.commit()
        return ImportFederationStatsResponseSchema(
            imported_players=result.imported_players,
            created_players=result.created_players,
            reused_players=result.reused_players,
            snapshots_created=result.snapshots_created,
            snapshots_skipped=result.snapshots_skipped,
            failed_rows=result.failed_rows,
            source_url=result.source_url,
            imported_at=result.imported_at,
        )
    except InvalidSourceUrlError as exc:
        _logger.error("invalid_source_url", detail=str(exc))
        return JSONResponse(status_code=400, content={"error": "INVALID_SOURCE_URL"})
    except HtmlFetchFailedError as exc:
        _logger.error("html_fetch_failed", detail=str(exc))
        return JSONResponse(status_code=502, content={"error": "HTML_FETCH_FAILED"})
    except TableStructureNotSupportedError as exc:
        _logger.error("table_structure_not_supported", detail=str(exc))
        return JSONResponse(status_code=422, content={"error": "TABLE_STRUCTURE_NOT_SUPPORTED"})
    except ImportFederationStatsError as exc:
        _logger.error("import_failed", detail=str(exc))
        return JSONResponse(status_code=500, content={"error": "IMPORT_FAILED"})
