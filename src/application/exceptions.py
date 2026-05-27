class ApplicationError(Exception):
    pass


class PlayerNotFoundError(ApplicationError):
    def __init__(self, player_id: object) -> None:
        super().__init__(f"Player not found: {player_id}")
        self.player_id = player_id
