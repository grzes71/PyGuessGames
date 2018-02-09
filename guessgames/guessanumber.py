"""
.. module:: guessgames.guessanumber
:platform: Unix, Windows
:synopsis: Guess a Number simple game.

.. moduleauthor:: Grzegorz Kotarski <gkotars@ra.rockwell.com>
"""

from guessgames.guessgame import GuessGame, time_print

GAME_NAME = "Guess a Number"


class GuessANumber(GuessGame):
    "Guess a Number game class."
    def __init__(self, number_to_guess, turns):
        "Initialize the game."
        super().__init__(GAME_NAME, turns=turns)
        self.__number_to_guess = number_to_guess
    
    @property
    def number_to_guess(self):
        "Get number to guess."
        return self.__number_to_guess

    def input_int(self, message, error_msg='This is not a numeric value, try again!'):
        """Get input from user until it can be casted to integer type.

        :param message: message to be displayed (user prompt).
        :type message: str
        :param error_msg: message to be displayed in case of error.
        :type error_msg: str        
        :return: value provided by user
        :rtype: int
        """
        while True:
            try:
                yield int(input(message))
            except ValueError:
                print(error_msg)

    def get_user_int(self, message):
        "get user input casted to int type."
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
        "Main game loop, executing game's logic."
        while self.turns:
            guess = self.get_user_int("Enter an integer from 1 to 99: ")
            if self.game_logic(guess):
                break
        else:
            self._print("Tries number exceeded, sorry {}!".format(self.username))


def main(number, turns=10):
        """Main game function.

        Creates and initializes the game objest, then run the game.

        :param number: number to guess.
        :type number: int
        :param turns: number of turns (defaults to 10).
        :type number: int
        """
    game = GuessANumber(number, turns)
    with time_print(GAME_NAME):
        game.play()

if __name__ == '__main__':
    from random import randint
    main(randint(0,100), 10)
