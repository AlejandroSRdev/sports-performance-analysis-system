from typing import Protocol
from uuid import UUID

from src.domain.entities.player import Player


class PlayerRepository(Protocol):

    def get_by_id(self, player_id: UUID) -> Player | None: ...

    def get_by_federation_player_id(self, federation_player_id: str) -> Player | None: ...

    def list_all(self) -> list[Player]: ...

    def save(self, player: Player) -> None: ...
