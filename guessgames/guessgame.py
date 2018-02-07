import time
from contextlib import contextmanager

class GuessGame:
    "Abstract Game base class."
    DEFAULT_WELCOME_MSG = "Hello {}, time to play {} game!"

    def __init__(self, name, turns, username="Unknown"):
        self.gamename = name
        self.turns = turns
        self.username = username

    @staticmethod
    def _input(message):
        "Generic input method."
        return input(message)

    @staticmethod
    def _print(message='', end='\n', sep=' '):
        print(message, end=end, sep=sep)

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

    def _set_user_name(self):
        self.username = self._input_name()

    def _welcome(self):
        "Display welcome message."
        self._print(self.__class__.DEFAULT_WELCOME_MSG.format(self.username, self.gamename))
        
    def game_loop(self):
        "Main game loop."
        return NotImplemented

    def play(self):
        "Play the game."
        self._set_user_name()        
        self._welcome()
        self.game_loop()
        self._game_over()

    def _game_over(self):
        "Game over."
        self._print('Game over !')


@contextmanager
def time_print(name):
    t = time.time() 
    try:
        yield
    finally:
        print("The {} game took {} seconds".format(name, time.time()-t))
