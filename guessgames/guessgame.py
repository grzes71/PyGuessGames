class GuessGame:
    "Abstract Game base class."
    DEFAULT_WELCOME_MSG = "Hello {}, time to play {} game!"

    def __init__(self, name, turns, username="Unknown"):
        self.gamename = name
        self.turns = turns
        self.username = username

    def hello(self):
        "Print game welcome message"
        print(self.__class__.DEFAULT_WELCOME_MSG.format(self.username, self.gamename))

    @staticmethod
    def _input(message):
        "Generic input method."
        return input(message)

    @staticmethod
    def _print(message):
        print(message)

    @property
    def turns(self):
        "Get number of turns"
        return self.__turns

    @turns.setter
    def turns(self, value):
        self.__turns = value

    @property
    def username(self):
        "Get user name."
        return self._username
    
    @property
    def gamename(self):
        "Get game name."
        return self._gamename 

    @gamename.setter
    def gamename(self, value):
        "Set game name."
        self._gamename = value.title()

    @username.setter
    def username(self, value):
        "Set user name."
        self._username = value.capitalize()

    def _input_name(self):
        "Method for getting user name."
        return self._input("What is your name? ")

    def set_user_name(self):
        self.username = self._input_name()

    def play(self):
        return NotImplemented
