from database_connection import get_database_connection


def drop_tables(connection):
    """Deletes database tables.

    Args: 
        connection (sqlite3.connection): sqlite database connection.
    """

    cursor = connection.cursor()

    cursor.execute("drop table if exists users")

    cursor.execute("drop table if exists games")

    connection.commit()


def create_tables(connection):
    """Creates database tables.

    Args: 
        connection (sqlite3.connection): sqlite database connection.
    """
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text,
            statuses text default "Backlog,Playing,Completed"
        );
    ''')

    cursor.execute('''
        create table games (
            id integer primary key,
            name text,
            status text,
            user text
        );
    ''')

    connection.commit()


def initialize_database():
    """Initializes database tables by deleting them and creating new ones.
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
