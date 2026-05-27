from src.domain.entities.player import Player
from src.infrastructure.database.models.player_model import PlayerModel


def to_domain(model: PlayerModel) -> Player:
    return Player(
        id=model.id,
        name=model.name,
        active=model.active,
        created_at=model.created_at,
        updated_at=model.updated_at,
        operational_identity_key=model.operational_identity_key,
        team=model.team,
        jersey_number=model.jersey_number,
    )


def to_model(entity: Player) -> PlayerModel:
    model = PlayerModel()
    model.id = entity.id
    model.name = entity.name
    model.active = entity.active
    model.created_at = entity.created_at
    model.updated_at = entity.updated_at
    model.operational_identity_key = entity.operational_identity_key
    model.team = entity.team
    model.jersey_number = entity.jersey_number
    return model
