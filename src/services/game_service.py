from entities.game import Game
from entities.user import User
from repositories.game_repository import game_repository
from repositories.user_repository import user_repository


class GameService:
    """Class that handles game and user related operations.
    """

    def __init__(self):
        """Constructor that initializes GameService with game and user repositories.

        Args:
            game_repository (GameRepository): Object that handles database operations for games.
            user_repository (UserRepository): Object that handles database operations for users.
        """
        self._game_repository = game_repository
        self._user_repository = user_repository
        self._logged_in_user = None

    def get_all_games(self):
        """Find all games associated with the currently logged-in user.

        Returns:
            List of Game objects that are associated with the user.
        """
        return self._game_repository.find_all_games_by_user(self._logged_in_user.username)

    def add_game_to_backlog(self, name, status):
        """Adds a new game to the backlog of the currently logged-in user.

        Args:
            name (str): The name of the game.
            status (str): The status assigned to the game.

        Returns:
           None.

        Raises:
            ValueError: If validating game input raises ValueError.
        """
        self._validate_game_input(name, status)

        game = Game(name, status, self._logged_in_user.username)
        return self._game_repository.add_game(game)

    def _validate_game_input(self, name, status):
        """Validates input for adding a new game.

        Args:
            name (str): The name of the game.
            status (str): The status assigned to the game.

        Raises:
            ValueError: If game name is empty.
            ValueError: If status name is empty.
            ValueError: If the game is already in the backlog.
        """
        if not name or name.strip() == "":
            raise ValueError("Game name can't be empty")
        if not status:
            raise ValueError("Choose status")
        if self._game_repository.find_game_by_user(name, self._logged_in_user.username):
            raise ValueError("Game already in backlog")

    def delete_game_from_backlog(self, name):
        """Deletes a game from the currently logged-in users backlog.

        Args:
            name (str): The name of the game.

        Returns:
            None.
        """
        return self._game_repository.delete_game(name, self._logged_in_user.username)

    def get_status_names(self):
        """Finds the status names associated with the currently logged-in user.

        Returns:
            List of the three status names associated with the user.
        """
        return self._user_repository.find_status_names(self._logged_in_user.username)

    def set_new_status_names(self, new_names):
        """Updates the status names associated with the currently logged-in user.

        Args:
            new_names (list[str]): List of three new status names.

        Raises:
            ValueError: If validating status names raises ValueError.
        """
        self._validate_status_names(new_names)

        old_names = self.get_status_names()
        status_dict = self._build_status_dict(old_names, new_names)

        self._update_status_names(status_dict)

        self._user_repository.change_status_names(
            new_names, self._logged_in_user.username)

    def _validate_status_names(self, new_names):
        """Validates list of new status names.

        Args:
            new_names (list[str]): List of three new status names.

        Raises:
            ValueError: If a status name is empty in the list.
            ValueError: If all status names are not unique.
        """
        for name in new_names:
            if name == "":
                raise ValueError("Status name can't be empty")
        if len(set(new_names)) < len(new_names):
            raise ValueError("Status names have to be unique")

    def _build_status_dict(self, old_names, new_names):
        """Create dictionary with old status names as keys to new status names.

        Args:
            old_names (list[str]): List of three current status names.
            new_names (list[str]): List of three new status names.

        Returns:
            Dictionary with old status names as keys to new status names.
        """
        status_dict = {}

        for i in range(len(old_names)):
            status_dict[old_names[i]] = new_names[i]

        return status_dict

    def _update_status_names(self, status_dict):
        """Update all games associated with the currently logged-in user with the new status names.

        Args:
            status_dict (dict): Dictionary with old status names as keys to new status names.
        """
        games = self.get_all_games()

        for game in games:
            # generoitu koodi alkaa
            new_name = status_dict.get(game.status)
            if new_name and new_name != game.status:
                # geneoroitu koodi päättyy
                self.change_game_status(game.name, new_name)

    def change_game_status(self, name, status):
        """Change the status of a game.

        Args:
            name (str): The name of the game.
            status (str): The status to be assigned to the game.

        Returns:
            None.
        """
        return self._game_repository.change_status(name, self._logged_in_user.username, status)

    def register_user(self, username, password):
        """Registers a new user.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.

        Raises:
            ValueError: If validating user registration raises ValueError.
            ValueError: If the user already exists.

        Returns:
            None.
        """
        username = username.strip()
        password = password.strip()

        self._validate_user_registration(username, password)

        user = User(username, password)
        if not self._user_repository.find_user(username):
            return self._user_repository.add_user(user)

        raise ValueError("User already exists")

    def _validate_user_registration(self, username, password):
        """Validates input of the registering user.

        Args:
            username (str): The username to be validated.
            password (str): The password to be validated.

        Raises:
            ValueError: If username is empty.
            ValueError: If password is empty.
        """
        if not username or username.strip() == "":
            raise ValueError("Username can't be empty")
        if not password or password.strip() == "":
            raise ValueError("Password can't be empty")

    def login(self, username, password):
        """Authenticates a user and logs them in.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Raises:
            ValueError: If username and password don't match or user doesn't exist.

        Returns:
            User object of the logged-in user.
        """
        user = self._user_repository.find_user(username)
        if user and user.password == password:
            self._logged_in_user = user
            return user

        raise ValueError("Wrong username or password")


game_service = GameService()
