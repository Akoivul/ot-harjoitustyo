from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        all_users = cursor.fetchall()
        users = []
        for user in all_users:
            users.append(User(user[0], user[1]))

        return users

    def find_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute("select * from users where username = ?", (username,))
        found_user = cursor.fetchone()

        if found_user:
            return User(found_user["username"], found_user["password"])

        return None

    def add_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("insert into users (username, password) values (?, ?)",
                       (user.username, user.password))
        self._connection.commit()
    
    def find_status_names(self, username):
        cursor = self._connection.cursor()
        cursor.execute("select statuses from users where username = ?", (username,))
        found_statuses = cursor.fetchone()

        return found_statuses["statuses"].split(",")
    
    def change_status_names(self, status_names, username):
        new_status_names = ",".join(status_names)
        cursor = self._connection.cursor()
        cursor.execute("update users set statuses = ? where username = ?", (new_status_names, username))
        self._connection.commit()


    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
