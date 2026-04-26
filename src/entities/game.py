class Game:
    """Class that represents a game.

    Attributes:
        name (str): The name of the game.
        status (str): The status of the game.
        user (str): The user that the game belongs to.
    """

    def __init__(self, name, status, user):
        """Constructor that initializes a game

        Args:
            name (str): The name of the game.
            status (str): The status of the game.
            user (str): The user that the game belongs to.
        """
        self.name = name
        self.status = status
        self.user = user
