from unittest.mock import patch
from unittest import TestCase

from guessgames.guessanumber import GuessANumber

class TestGuessaNumber(TestCase):

    def setUp(self):
        self.game = GuessANumber(50, turns=10)

    def test_get_user_input(self):
        with patch('builtins.input', return_value=10):
            guess = self.game.get_user_input()
            self.assertEqual(guess, 10)

    def test_game_logic_too_low(self):
        with patch('builtins.input', return_value=49):
            with patch.object(self.game, '_print') as mock:
                guess = self.game.game_logic(49)
                self.assertFalse(guess)
                mock.assert_called_with("Your guess is too low")
                self.assertEqual(self.game.turns, 9)

    def test_game_logic_too_high(self):
        with patch('builtins.input', return_value=51):
            with patch.object(self.game, '_print') as mock:
                guess = self.game.game_logic(51)
                self.assertFalse(guess)
                mock.assert_called_with("Your guess is too high")
                self.assertEqual(self.game.turns, 9)

    def test_game_logic_success(self):
        with patch('builtins.input', return_value=50):
            with patch.object(self.game, '_print') as mock:
                guess = self.game.game_logic(50)
                self.assertTrue(guess)
                mock.assert_called_with("You guessed it!")
                self.assertEqual(self.game.turns, 10)

    def test_play_game_loop_success(self):
        with patch('builtins.input', return_value=50):
            with patch.object(self.game, 'game_logic') as mock_game:
                self.game.play_game()
                mock_game.assert_called_with(50)

    def test_play_game_loop_failure(self):
        with patch('builtins.input', return_value=0):
            with patch.object(self.game, 'game_logic') as mock_game:
                self.game.play_game()
                mock_game.assert_called_with(0)
