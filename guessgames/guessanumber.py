"""
.. module:: guessgames.guessanumber
:platform: Unix, Windows
:synopsis: Guess a Number simple game.

.. moduleauthor:: FullName <email>
"""
class GuessANumber:
    def __init__(self, number_to_guess, turns=10):
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
        while True:
            try:
                return int(input("Enter an integer from 1 to 99: "))
            except ValueError:
                self._print('This is not a numeric value, try again!')

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
            self._print("You guessed it!")
            return True
        self.turns -= 1

    def play_game(self):
        while self.turns:
            guess = self.get_user_input()
            if self.game_logic(guess):
                break
        else:
            self._print("Tries number exceeded, sorry!")

    def play(self):
        self.play_game()
        self._print("Game over")


def main():
    game = GuessANumber(50)
    game.play()


if __name__ == '__main__':
    main()
