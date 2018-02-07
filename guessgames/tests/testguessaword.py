from unittest.mock import patch
from unittest import TestCase, main

from guessgames.guessaword import GuessAWord

class TestGuessAWord(TestCase):

    def setUp(self):
        self.game = GuessAWord('secret', 10)

    def test_getturns(self):
        self.assertEqual(self.game.turns, 10)

    def test_setturns(self):
        self.game.turns -= 1
        self.assertEqual(self.game.turns, 9)

    def test_number_to_guess(self):
        self.assertEqual(self.game.word_to_guess, 'SECRET')

    def test_getgamename(self):
        self.assertEqual(self.game.gamename, 'Guess A Word')

    def test_getusername(self):
        self.assertEqual(self.game.username, 'Unknown')

    def test_setusername(self):
        self.game.username = 'greg'
        self.assertEqual(self.game.username, 'Greg')


if __name__ == '__main__':
    main()
