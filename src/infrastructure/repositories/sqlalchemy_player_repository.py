from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.player import Player
from src.infrastructure.database.mappers import player_mapper
from src.infrastructure.database.models.player_model import PlayerModel


class SQLAlchemyPlayerRepository:

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, player_id: UUID) -> Player | None:
        stmt = select(PlayerModel).where(PlayerModel.id == player_id)
        model = self._session.execute(stmt).scalar_one_or_none()
        if model is None:
            return None
        return player_mapper.to_domain(model)

    def get_by_federation_player_id(self, federation_player_id: str) -> Player | None:
        # federation_player_id is not persisted in the current schema;
        # this method exists to satisfy the repository contract for future use.
        raise NotImplementedError(
            "federation_player_id is not stored in the current schema."
        )

    def find_by_operational_identity_key(self, operational_identity_key: str) -> Player | None:
        stmt = select(PlayerModel).where(
            PlayerModel.operational_identity_key == operational_identity_key
        )
        model = self._session.execute(stmt).scalar_one_or_none()
        if model is None:
            return None
        return player_mapper.to_domain(model)

    def list_all(self) -> list[Player]:
        stmt = select(PlayerModel).order_by(PlayerModel.created_at.asc())
        models = self._session.execute(stmt).scalars().all()
        return [player_mapper.to_domain(m) for m in models]

    def save(self, player: Player) -> None:
        model = player_mapper.to_model(player)
        self._session.merge(model)
