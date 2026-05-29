import re
import unicodedata


class OperationalIdentityBuilder:
    """Deterministic service that normalizes player attributes and builds an operational identity key."""

    @staticmethod
    def normalize_text(value: str) -> str:
        nfkd = unicodedata.normalize("NFKD", value)
        ascii_text = nfkd.encode("ascii", "ignore").decode("ascii")
        lowered = ascii_text.lower().strip()
        return re.sub(r"\s+", "_", lowered)

    @classmethod
    def build(
        cls,
        *,
        name: str,
        team: str | None,
    ) -> str:
        normalized_name = cls.normalize_text(name)
        team_part = cls.normalize_text(team) if team is not None else "unknown"
        return f"{normalized_name}:{team_part}"
