import unittest
from repositories.game_repository import game_repository
from repositories.user_repository import user_repository
from services.game_service import game_service


class TestGameService(unittest.TestCase):
    def setUp(self):
        game_repository.delete_all()
        user_repository.delete_all()

    def test_register_user_successfully(self):
        game_service.register_user("test_username1", "test_password1")
        user = user_repository.find_user("test_username1")

        self.assertEqual(user.username, "test_username1")

    def test_register_user_when_user_already_exists(self):
        game_service.register_user("test_username1", "test_password1")

        with self.assertRaises(Exception):
            game_service.register_user("test_username1", "test_password2")
