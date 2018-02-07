"""
.. module:: guessgames.guessanumber
:platform: Unix, Windows
:synopsis: Guess a Number simple game.

.. moduleauthor:: FullName <email>
"""

from contextlib import contextmanager
from guessgames.guessgame import GuessGame


class GuessANumber(GuessGame):
    "Guess a Number game class."
    def __init__(self, number_to_guess, turns=10):
        "Initialize the game."
        super().__init__("Guess a Number")
        self.__number_to_guess = number_to_guess
        self.__turns = turns
    
    @property
    def number_to_guess(self):
        "Get number to guess."
        return self.__number_to_guess

    @property
    def turns(self):
        "Get number of turns"
        return self.__turns

    @turns.setter
    def turns(self, value):
        self.__turns = value

    def input_int(self, message, error_msg='This is not a numeric value, try again!'):
        while True:
            try:
                yield int(input(message))
            except ValueError:
                print(error_msg)

    def get_user_int(self, message):
        return next(self.input_int(message)) 

    def game_logic(self, guess):
        """Implements the game logic.

        Displays an appropriate message if the 
        guessed number is lower, higher or 
        exactly the number to guess - 
        returns True in this case, 
        otherwise decreases number of turns.

        :param guess: number provided by player.
        :type guess: int
        :return: True if number is correct.
        """
        if guess < self.number_to_guess:
            self._print("Your guess is too low")
        elif guess > self.number_to_guess:
            self._print("Your guess is too high")
        else:
            self._print("You guessed it {}!".format(self.username))
            return True
        self.turns -= 1

    def game_loop(self):
        "Main game loop."
        while self.turns:
            guess = self.get_user_int("Enter an integer from 1 to 99: ")
            if self.game_logic(guess):
                break
        else:
            self._print("Tries number exceeded, sorry {}!".format(self.username))

    def play(self):
        "Play the game."
        self.set_user_name()
        self.game_loop()
        self._print("Game over")


def main(number, turns):
    game = GuessANumber(number, turns)
    game.play()


if __name__ == '__main__':
    from random import randint
    main(randint(0,100), 10)
