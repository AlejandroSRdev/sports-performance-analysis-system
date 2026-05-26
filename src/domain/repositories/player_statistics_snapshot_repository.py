from datetime import date
from typing import Protocol
from uuid import UUID

from src.domain.entities.player_statistics_snapshot import PlayerStatisticsSnapshot


class PlayerStatisticsSnapshotRepository(Protocol):

    def save(self, snapshot: PlayerStatisticsSnapshot) -> None: ...

    def list_by_player_id(self, player_id: UUID) -> list[PlayerStatisticsSnapshot]: ...

    def list_between_dates(
        self,
        player_id: UUID,
        start_date: date,
        end_date: date,
    ) -> list[PlayerStatisticsSnapshot]: ...

    def get_latest_by_player_id(self, player_id: UUID) -> PlayerStatisticsSnapshot | None: ...
