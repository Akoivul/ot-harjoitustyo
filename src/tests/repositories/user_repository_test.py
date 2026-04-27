import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.test_user_1 = User("testing user_1", "test_password1")
        self.test_user_2 = User("testing user_2", "test_password2")
        user_repository.add_user(self.test_user_1)

    def test_add_user(self):
        users = user_repository.find_all_users()
        username = users[0].username
        password = users[0].password

        self.assertEqual(len(users), 1)
        self.assertEqual(username, self.test_user_1.username)
        self.assertEqual(password, self.test_user_1.password)

    def test_find_all_users(self):
        user_repository.add_user(self.test_user_2)
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.test_user_1.username)
        self.assertEqual(users[0].password, self.test_user_1.password)
        self.assertEqual(users[1].username, self.test_user_2.username)
        self.assertEqual(users[1].password, self.test_user_2.password)

    def test_find_user_found(self):
        user_repository.add_user(self.test_user_2)
        user = user_repository.find_user(self.test_user_1.username)

        self.assertEqual(user.username, self.test_user_1.username)
        self.assertEqual(user.password, self.test_user_1.password)

    def test_find_status_names(self):
        status_names = user_repository.find_status_names(
            self.test_user_1.username)

        self.assertEqual(status_names[0], "Backlog")
        self.assertEqual(status_names[1], "Playing")
        self.assertEqual(status_names[2], "Completed")

    def test_change_status_names(self):
        new_status_names = ["Wishlist", "In progress", "Finished"]
        user_repository.change_status_names(
            new_status_names, self.test_user_1.username)
        changed_status_names = user_repository.find_status_names(
            self.test_user_1.username)

        self.assertEqual(changed_status_names, new_status_names)
