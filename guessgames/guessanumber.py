"""
.. module:: guessgames.guessanumber
:platform: Unix, Windows
:synopsis: Guess a Number simple game.

.. moduleauthor:: FullName <email>
"""

from guessgames.guessgame import GuessGame


class InputManager:
    def __init__(self, message):
        self.message = message
    def __enter__(self):
        while True:
            try:
                return int(input(self.message))
            except ValueError:
                print('This is not a numeric value, try again!')
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class GuessANumber(GuessGame):
    "Guess a word game class."
    def __init__(self, number_to_guess, turns=10):
        super().__init__("Guess a Number")
        self.__number_to_guess = number_to_guess
        self.__turns = turns
    
    @property
    def number_to_guess(self):
        return self.__number_to_guess

    @property
    def turns(self):
        return self.__turns

    @turns.setter
    def turns(self, value):
        self.__turns = value

    def _print(self, message):
        print(message)

    def get_user_input(self):
        with InputManager("Enter an integer from 1 to 99: ") as value:
                return value

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

    def play_game(self):
        while self.turns:
            guess = self.get_user_input()
            if self.game_logic(guess):
                break
        else:
            self._print("Tries number exceeded, sorry {}!".format(self.username))

    def play(self):
        self.play_game()
        self._print("Game over")


def main(number, turns):
    game = GuessANumber(number, turns)
    game.play()


if __name__ == '__main__':
    from random import randint
    main(randint(0,100), 10)
