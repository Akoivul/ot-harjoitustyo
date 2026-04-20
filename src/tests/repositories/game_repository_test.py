import unittest
from repositories.game_repository import game_repository
from entities.game import Game


class TestGameRepository(unittest.TestCase):
    def setUp(self):
        game_repository.delete_all()
        self.test_game_1 = Game("testing game_1", "Backlog", "user1")
        self.test_game_2 = Game("testing game_2", "In progress", "user2")

    def test_add_game(self):
        game_repository.add_game(self.test_game_1)
        games = game_repository.find_all_games_by_user(self.test_game_1.user)
        game_name = games[0].name
        game_status = games[0].status

        self.assertEqual(len(games), 1)
        self.assertEqual(game_name, self.test_game_1.name)
        self.assertEqual(game_status, self.test_game_1.status)

    def test_delete_game(self):
        game_repository.add_game(self.test_game_1)
        games = game_repository.find_all_games_by_user(self.test_game_1.user)
        game_name = games[0].name
        game_user = games[0].user

        self.assertEqual(len(games), 1)

        game_repository.delete_game(game_name, game_user)
        games = game_repository.find_all_games_by_user(self.test_game_1.user)

        self.assertEqual(len(games), 0)

    def test_find_all_games_by_user(self):
        game_repository.add_game(self.test_game_1)
        game_repository.add_game(self.test_game_2)
        games_1 = game_repository.find_all_games_by_user(self.test_game_1.user)
        games_2 = game_repository.find_all_games_by_user(self.test_game_2.user)

        self.assertEqual(len(games_1), 1)
        self.assertEqual(len(games_2), 1)
        self.assertEqual(games_1[0].name, self.test_game_1.name)
        self.assertEqual(games_1[0].status, self.test_game_1.status)
        self.assertEqual(games_2[0].name, self.test_game_2.name)
        self.assertEqual(games_2[0].status, self.test_game_2.status)

    def test_find_game_by_user(self):
        game_repository.add_game(self.test_game_1)
        game = game_repository.find_game_by_user(
            self.test_game_1.name, self.test_game_1.user)

        self.assertEqual(game.name, self.test_game_1.name)
        self.assertEqual(game.status, self.test_game_1.status)
        self.assertEqual(game.user, self.test_game_1.user)

    def test_change_status(self):
        game_repository.add_game(self.test_game_1)
        game_repository.add_game(self.test_game_2)
        game_repository.change_status(
            self.test_game_1.name, self.test_game_1.user, "Finished")
        game_1 = game_repository.find_game_by_user(
            self.test_game_1.name, self.test_game_1.user)
        game_2 = game_repository.find_game_by_user(
            self.test_game_2.name, self.test_game_2.user)

        self.assertEqual(game_1.status, "Finished")
        self.assertEqual(game_2.status, "In progress")
