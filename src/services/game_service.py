from entities.game import Game
from entities.user import User
from repositories.game_repository import game_repository
from repositories.user_repository import user_repository


class GameService:
    def __init__(self, game_repository, user_repository):
        self._game_repository = game_repository
        self._user_repository = user_repository
        self._logged_in_user = None
    
    def get_all_games(self):
        return self._game_repository.find_all_games_by_user(self._logged_in_user.username)

    def add_game_to_backlog(self, name, state):
        if self._game_repository.find_game_by_user(name, self._logged_in_user.username):
            raise ValueError("Game already in backlog")
        
        game = Game(name, state, self._logged_in_user.username)
        return self._game_repository.add_game(game)

    def delete_game_from_backlog(self, name):
        return self._game_repository.delete_game(name)

    def register_user(self, username, password):
        if not username or username.strip() == "":
            raise ValueError("Username can't be empty")
        
        user = User(username.strip(), password.strip())
        if not self._user_repository.find_user(username):
            return self._user_repository.add_user(user)

        raise ValueError("User already exists")

    def login(self, username, password):
        user = self._user_repository.find_user(username)
        if user and user.password == password:
            self._logged_in_user = user
            return user
        
        raise ValueError("Wrong username or password")



game_service = GameService(game_repository, user_repository)
