from entities.game import Game
from entities.user import User
from repositories.game_repository import game_repository
from repositories.user_repository import user_repository


class GameService:
    def __init__(self, game_repository, user_repository):
        self._game_repository = game_repository
        self._user_repository = user_repository

    def add_game_to_backlog(self, name, state):
        game = Game(name, state)

        return self._game_repository.add_game(game)

    def delete_game_from_backlog(self, name):
        return self._game_repository.delete_game(name)

    def register_user(self, username, password):
        if self._user_repository.find_user(username):
            raise Exception("User already exists")

        user = User(username, password)
        return self._user_repository.add_user(user)


game_service = GameService(game_repository, user_repository)
