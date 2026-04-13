from entities.game import Game
from database_connection import get_database_connection


class GameRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all_games_by_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("select * from games where user = ?", (user,))
        all_games = cursor.fetchall()
        games = []
        for game in all_games:
            games.append(Game(game[0], game[1], game[2]))

        return games

    def find_game_by_user(self, name, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from games where name = ? and user = ?", (name, user,))
        found_game = cursor.fetchone()

        if found_game:
            return Game(found_game["name"], found_game["status"], found_game["user"])

        return None

    def add_game(self, game):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into games (name, status, user) values (?, ?, ?)", (game.name, 
                                                                        game.status, game.user,))
        self._connection.commit()

    def delete_game(self, name):
        cursor = self._connection.cursor()
        cursor.execute("delete from games where name = ?", (name,))
        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from games")
        self._connection.commit()

    def change_status(self):
        pass


game_repository = GameRepository(get_database_connection())
