from unittest.mock import patch
from unittest import TestCase, main

from guessgames.guessaword import GuessAWord

class TestGuessAWord(TestCase):

    def setUp(self):
        self.game = GuessAWord('secret', 10)



if __name__ == '__main__':
    main()
