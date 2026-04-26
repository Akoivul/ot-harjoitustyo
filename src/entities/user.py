class User:
    """ Class that represents a user

    Attributes:
        username (str): the username of the user
        password (str): the password of the user
    """

    def __init__(self, username, password):
        """Constructor that initializes a user

        Args:
            username (str): the username of the user
            password (str): the password of the user
        """
        self.username = username
        self.password = password
