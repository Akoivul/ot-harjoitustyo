import unittest
from repositories.game_repository import game_repository
from entities.game import Game


class TestGameRepository(unittest.TestCase):
    def setUp(self):
        game_repository.delete_all()
        self.test_game_1 = Game("testing game_1", "Backlog")
        self.test_game_2 = Game("testing game_2", "In progress")

    def test_add_game(self):
        game_repository.add_game(self.test_game_1)
        games = game_repository.find_all_games()
        game_name = games[0].name
        game_status = games[0].status

        self.assertEqual(len(games), 1)
        self.assertEqual(game_name, self.test_game_1.name)
        self.assertEqual(game_status, self.test_game_1.status)

    def test_delete_game(self):
        game_repository.add_game(self.test_game_1)
        games = game_repository.find_all_games()
        game_name = games[0].name

        self.assertEqual(len(games), 1)

        game_repository.delete_game(game_name)
        games = game_repository.find_all_games()

        self.assertEqual(len(games), 0)

    def test_find_all_games(self):
        game_repository.add_game(self.test_game_1)
        game_repository.add_game(self.test_game_2)
        games = game_repository.find_all_games()

        self.assertEqual(len(games), 2)
        self.assertEqual(games[0].name, self.test_game_1.name)
        self.assertEqual(games[0].status, self.test_game_1.status)
        self.assertEqual(games[1].name, self.test_game_2.name)
        self.assertEqual(games[1].status, self.test_game_2.status)
