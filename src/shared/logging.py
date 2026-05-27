import json
import logging


def get_logger(name: str) -> "StructuredLogger":
    return StructuredLogger(logging.getLogger(name))


class StructuredLogger:
    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger

    def _serialize(self, event: str, **kwargs: object) -> str:
        return json.dumps({"event": event, **kwargs}, default=str)

    def info(self, event: str, **kwargs: object) -> None:
        self._logger.info(self._serialize(event, **kwargs))

    def warning(self, event: str, **kwargs: object) -> None:
        self._logger.warning(self._serialize(event, **kwargs))

    def error(self, event: str, **kwargs: object) -> None:
        self._logger.error(self._serialize(event, **kwargs))
