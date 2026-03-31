from entities.game import Game
from database_connection import get_database_connection

class GameRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def find_all_games(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from games")
        all_games = cursor.fetchall()
        games = []
        for game in all_games:
            games.append(Game(game[0], game[1]))
        
        return games

    def add_game(self, game):
        cursor = self._connection.cursor()
        cursor.execute("insert into games (name, state) values (?, ?)", (game.name, game.status))
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