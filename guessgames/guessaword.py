"""
.. module:: guessgames.guessanumber
:platform: Unix, Windows
:synopsis: Guess a NumbWorder simple game.

.. moduleauthor:: FullName <email>
"""

from guessgames.guessgame import GuessGame, time_print

GAME_NAME = "Guess a Word"

class GuessAWord(GuessGame):
    "Guess a word game class."
    def __init__(self, word, turns):
        super().__init__(GAME_NAME, turns=turns)
        self.word_to_guess = word
        self.guesses = []
    
    @property
    def word_to_guess(self):
        return self._word_to_guess

    @word_to_guess.setter
    def word_to_guess(self, value):
        self._word_to_guess = value.upper()

    def generate_chars(self, guessed_chars):
        for c in self.word_to_guess:
            if c in guessed_chars:
                yield c
            else:
                yield '_'
        
    def print_chars(self, guessed_chars):
        for c in self.generate_chars(guessed_chars):
            self._print(c, end='')
        self._print()

    def game_logic(self, user_char, guessed_chars):
        if user_char in guessed_chars:
            self._print('Character already guessed!')
        elif user_char in self.word_to_guess:
            self._print('Good job!')
            guessed_chars.add(user_char)
            if guessed_chars == set(self.word_to_guess):
                self._print('The word is "{}", congratulations {}'.format(self.word_to_guess, self.username))
                return True
        else:
            self._print('Sorry!')

    def game_loop(self):
        guessed_chars = set()
        while self.turns:
            self.print_chars(guessed_chars)
            user_char = self._input("Enter character: ").upper()
            if self.game_logic(user_char, guessed_chars):
                break
            self.turns -= 1
        else:
            self._print('You did not guess the word: {}'.format(self.word_to_guess))


def main(word, turns=10):
    game = GuessAWord(word, turns)
    with time_print(GAME_NAME):
        game.play()

if __name__ == '__main__':    
    main('secret')

