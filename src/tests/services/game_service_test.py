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
        self.default_statuses = ["Backlog", "Playing", "Completed"]

    def test_register_user_successfully(self):
        game_service.register_user("test_username2", "test_password2")
        user = user_repository.find_user("test_username2")

        self.assertEqual(user.username, "test_username2")

    def test_register_user_when_user_already_exists(self):
        with self.assertRaises(Exception):
            game_service.register_user("test_username1", "test_password2")

    def test_register_user_when_username_empty(self):
        with self.assertRaises(Exception):
            game_service.register_user("", "test_password2")

    def test_register_user_when_password_empty(self):
        with self.assertRaises(Exception):
            game_service.register_user("test_username2", "")

    def test_login_successfully(self):
        user = game_service.login("test_username1", "test_password1")

        self.assertEqual(user.username, "test_username1")

    def test_login_when_user_is_not_registered(self):
        with self.assertRaises(Exception):
            game_service.login("test_username3", "test_password3")

    def test_add_game_to_backlog_successfully(self):
        game_service.login("test_username1", "test_password1")
        game_service.add_game_to_backlog("test_game", self.default_statuses[1])
        games = game_service.get_all_games()

        self.assertEqual(games[0].name, "test_game")
        self.assertEqual(games[0].status, self.default_statuses[1])

    def test_add_game_to_backlog_when_game_is_already_in_backlog(self):
        game_service.login("test_username1", "test_password1")
        game_service.add_game_to_backlog("test_game", self.default_statuses[0])

        with self.assertRaises(Exception):
            game_service.add_game_to_backlog(
                "test_game", self.default_statuses[0])

    def test_add_game_with_empty_name_to_backlog(self):
        game_service.login("test_username1", "test_password1")

        with self.assertRaises(Exception):
            game_service.add_game_to_backlog("", self.default_statuses[1])

    def test_add_game_with_no_status_to_backlog(self):
        game_service.login("test_username1", "test_password1")

        with self.assertRaises(Exception):
            game_service.add_game_to_backlog("test_game", "")

    def test_delete_game_from_backlog(self):
        game_service.login("test_username1", "test_password1")
        game_service.add_game_to_backlog("test_game", self.default_statuses[1])
        games = game_service.get_all_games()

        self.assertEqual(len(games), 1)

        game_service.delete_game_from_backlog("test_game")
        games = game_service.get_all_games()

        self.assertEqual(len(games), 0)

    def test_set_new_status_names_successfully(self):
        game_service.login("test_username1", "test_password1")
        new_status_names = ["Wishlist", "Currently playing", "Finished"]
        game_service.set_new_status_names(new_status_names)

        changed_status_names = game_service.get_status_names()

        self.assertEqual(new_status_names, changed_status_names)

    def test_set_new_status_names_with_empty_status(self):
        game_service.login("test_username1", "test_password1")
        new_status_names = ["Wishlist", "Currently playing", ""]

        with self.assertRaises(Exception):
            game_service.set_new_status_names(new_status_names)

    def test_set_new_status_names_with_duplicate_status_names(self):
        game_service.login("test_username1", "test_password1")
        new_status_names = ["Wishlist", "Finished", "Finished"]

        with self.assertRaises(Exception):
            game_service.set_new_status_names(new_status_names)

    def test_setting_new_status_names_updates_status_of_added_games(self):
        game_service.login("test_username1", "test_password1")
        game_service.add_game_to_backlog("test_game", self.default_statuses[1])
        new_status_names = ["Wishlist", "Currently playing", "Finished"]
        game_service.set_new_status_names(new_status_names)

        games = game_service.get_all_games()
        self.assertEqual(games[0].status, new_status_names[1])
