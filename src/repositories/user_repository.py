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
    
    def add_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("insert into users (username, password) values (?, ?)", (user.username, user.password))
        self._connection.commit()

user_repository = UserRepository(get_database_connection())