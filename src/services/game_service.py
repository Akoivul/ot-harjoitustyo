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

    def add_game_to_backlog(self, name, status):
        self._validate_game_input(name, status)

        game = Game(name, status, self._logged_in_user.username)
        return self._game_repository.add_game(game)
    
    def _validate_game_input(self, name, status):
        if not name or name.strip() == "":
            raise ValueError("Game name can't be empty")
        if not status:
            raise ValueError("Choose status")
        if self._game_repository.find_game_by_user(name, self._logged_in_user.username):
            raise ValueError("Game already in backlog")

    def delete_game_from_backlog(self, name):
        return self._game_repository.delete_game(name, self._logged_in_user.username)
    
    def get_status_names(self):
        return self._user_repository.find_status_names(self._logged_in_user.username)
    
    def set_new_status_names(self, new_names):
        self._validate_status_names(new_names)

        old_names = self.get_status_names()
        status_dict = self._build_status_dict(old_names, new_names)

        self._update_status_names(status_dict)

        self._user_repository.change_status_names(new_names, self._logged_in_user.username)

    def _validate_status_names(self, new_names):
        for name in new_names:
            if name == "":
                raise ValueError("Status name can't be empty")
        if len(set(new_names)) < len(new_names):
            raise ValueError("Status names have to be unique")
    
    def _build_status_dict(self, old_names, new_names):
        status_dict = {}

        for i in range(len(old_names)):
            status_dict[old_names[i]] = new_names[i]

        return status_dict
    
    def _update_status_names(self, status_dict):
        games = self.get_all_games()
        
        for game in games:
# generoitu koodi alkaa
            new_name = status_dict.get(game.status)
            if new_name and new_name != game.status:
# geneoroitu koodi päättyy
                self.change_game_status(game.name, new_name)

    def change_game_status(self, name, status):
        return self._game_repository.change_status(name, self._logged_in_user.username, status)

    def register_user(self, username, password):
        username = username.strip()
        password = password.strip()

        self._validate_user_registration(username, password)

        user = User(username, password)
        if not self._user_repository.find_user(username):
            return self._user_repository.add_user(user)

        raise ValueError("User already exists")
    
    def _validate_user_registration(self, username, password):
        if not username or username.strip() == "":
            raise ValueError("Username can't be empty")
        if not password or password.strip() == "":
            raise ValueError("Password can't be empty")

    def login(self, username, password):
        user = self._user_repository.find_user(username)
        if user and user.password == password:
            self._logged_in_user = user
            return user

        raise ValueError("Wrong username or password")


game_service = GameService(game_repository, user_repository)
