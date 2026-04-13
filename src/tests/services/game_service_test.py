import unittest
from repositories.game_repository import game_repository
from repositories.user_repository import user_repository
from services.game_service import game_service


class TestGameService(unittest.TestCase):
    def setUp(self):
        game_repository.delete_all()
        user_repository.delete_all()
        self.test_registered_user = game_service.register_user(
            "test_username1", "test_password1")

    def test_register_user_successfully(self):
        user = user_repository.find_user("test_username1")

        self.assertEqual(user.username, "test_username1")

    def test_register_user_when_user_already_exists(self):
        with self.assertRaises(Exception):
            game_service.register_user("test_username1", "test_password2")

    def test_login_successfully(self):
        user = game_service.login("test_username1", "test_password1")

        self.assertEqual(user.username, "test_username1")

    def test_login_when_user_is_not_registered(self):
        with self.assertRaises(Exception):
            game_service.login("test_username3", "test_password3")

    def test_add_game_to_backlog_successfully(self):
        game_service.login("test_username1", "test_password1")
        game_service.add_game_to_backlog("test_game", "in progress")
        games = game_service.get_all_games()

        self.assertEqual(games[0].name, "test_game")
        self.assertEqual(games[0].status, "in progress")

    def test_add_game_to_backlog_when_game_is_already_in_backlog(self):
        game_service.login("test_username1", "test_password1")
        game_service.add_game_to_backlog("test_game", "in progress")

        with self.assertRaises(Exception):
            game_service.add_game_to_backlog("test_game", "in progress")
