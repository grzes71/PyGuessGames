from unittest.mock import patch, call
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

    def test_generate_chars(self):
        guessed_chars = set('ST')
        chars_generator = self.game.generate_chars(guessed_chars)
        generated_chars = ''.join(chars_generator)
        self.assertEqual(generated_chars, 'S____T')

    def test_print(self):
        with patch('builtins.print') as mock:
            self.game._print("Hello", end='', sep='-')
            mock.assert_called_with("Hello", end='', sep='-')

    def test_print_chars(self):
        guessed_chars = set('ST')
        with patch.object(self.game, '_print') as mock_print:
            self.game.print_chars(guessed_chars)
            expected = [call('S', end=''), call('_', end=''), call('_', end=''), 
                        call('_', end=''), call('_', end=''), call('T', end=''), call()]            
            self.assertEqual(mock_print.mock_calls, expected)

    def test_game_logic_success(self):
        self.game.username = 'greg'
        guessed_chars = set('SECRE')
        user_char = 'T'
        with patch.object(self.game, '_print') as mock:
            guess = self.game.game_logic(user_char, guessed_chars)
            self.assertTrue(guess)
            mock.assert_called_with('The word is "{}", congratulations {}'.format('SECRET', 'Greg'))
            self.assertEqual(self.game.turns, 10)

if __name__ == '__main__':
    main()
