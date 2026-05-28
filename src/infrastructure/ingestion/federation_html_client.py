import requests
from src.infrastructure.ingestion.exceptions import HtmlFetchFailedError


class FederationHtmlClient:

    def fetch(self, source_url: str) -> str:
        try:
            response = requests.get(source_url, timeout=15)
            response.raise_for_status()
            return response.text
        except requests.RequestException as exc:
            raise HtmlFetchFailedError(str(exc)) from exc
