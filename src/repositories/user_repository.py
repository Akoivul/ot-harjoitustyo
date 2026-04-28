from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """Class that handles database operations for users.
    """

    def __init__(self, connection):
        """Constructor that initializes UserRepository.

        Args:
            connection (sqlite3.connection): sqlite database connection.
        """
        self._connection = connection

    def find_all_users(self):
        """Finds all users.

        Returns:
            List of User objects.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        all_users = cursor.fetchall()
        users = []
        for user in all_users:
            users.append(User(user[0], user[1]))

        return users

    def find_user(self, username):
        """Finds a user by username.

        Args:
            username (str): The username of the user.

        Returns:
            User object if the user is found and otherwise None.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from users where username = ?", (username,))
        found_user = cursor.fetchone()

        if found_user:
            return User(found_user["username"], found_user["password"])

        return None

    def add_user(self, user):
        """Adds a new user to the database.

        Args:
            user (User): The User object to be added to the database.
        """
        cursor = self._connection.cursor()
        cursor.execute("insert into users (username, password) values (?, ?)",
                       (user.username, user.password))
        self._connection.commit()

    def find_status_names(self, username):
        """Finds the status names associated with a given user.

        Args:
            username (str): The username of the user.

        Returns:
            List that contains three status names.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "select statuses from users where username = ?", (username,))
        found_statuses = cursor.fetchone()

        return found_statuses["statuses"].split(",")

    def change_status_names(self, status_names, username):
        """Changes the status names associated with a given user.

        Args:
            status_names (list[str]): List with three status names to be updated to the database.
            username (str): The username of the user.
        """
        new_status_names = ",".join(status_names)
        cursor = self._connection.cursor()
        cursor.execute(
            "update users set statuses = ? where username = ?", (new_status_names, username))
        self._connection.commit()

    def delete_all(self):
        """Deletes all users from the database.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
