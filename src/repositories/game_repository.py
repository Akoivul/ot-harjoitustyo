from entities.game import Game
from database_connection import get_database_connection


class GameRepository:
    """Class that handles database operations for games.
    """

    def __init__(self, connection):
        """Constructor that initializes GameRepository.

        Args:
            connection (sqlite3.connection): sqlite database connection.
        """
        self._connection = connection

    def find_all_games_by_user(self, user):
        """Finds all games associated with a user

        Args:
            user (str): The username of the user

        Returns:
            List of Game objects that are associated with the user.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from games where user = ?", (user,))
        all_games = cursor.fetchall()
        games = []
        for game in all_games:
            games.append(Game(game["name"], game["status"], game["user"]))

        return games

    def find_game_by_user(self, name, user):
        """Finds a specific game associated with a given user.

        Args:
            name (str): The name of the game.
            user (str): The username of the user.

        Returns:
            Game object if the game is found and otherwise None.

        """
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from games where name = ? and user = ?", (name, user,))
        found_game = cursor.fetchone()

        if found_game:
            return Game(found_game["name"], found_game["status"], found_game["user"])

        return None

    def add_game(self, game):
        """Adds a new game to the database.

        Args:
            game (Game): The Game object to be added to the database.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into games (name, status, user) values (?, ?, ?)", (game.name,
                                                                        game.status, game.user,))
        self._connection.commit()

    def delete_game(self, name, user):
        """Deletes a game associated with a given user.

        Args:
            name (str): The name of the game to be deleted.
            user (str): The username of the user.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "delete from games where name = ? and user = ?", (name, user,))
        self._connection.commit()

    def delete_all(self):
        """Deletes all games from the database.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from games")
        self._connection.commit()

    def change_status(self, name, user, status):
        """Changes the status of a game associated with a given user.

        Args:
            name (str): The name of the game.
            user (str): The username of the user.
            status (str): The new status to be given to the game.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "update games set status = ? where name = ? and user = ?", (status, name, user, ))
        self._connection.commit()


game_repository = GameRepository(get_database_connection())
