from unittest.mock import patch
from unittest import TestCase

from guessgame.guessanumber import GuessANumber

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
            with patch.object(self.game, 'game_logic') as mock:
                with patch.object(self.game, '_print') as mock_print:
                    self.game.play_game()
                    mock.assert_called_with(50)
                    mock_print.assert_called_with("Game over")
                    self.assertEqual(self.game.turns, 10)

    def test_play_game_loop_failure(self):
        with patch('builtins.input', return_value=0):
            with patch.object(self.game, 'game_logic') as mock:
                with patch.object(self.game, '_print') as mock_print:
                    self.game.play_game()
                    mock.assert_called_with(0)
                    mock_print.assert_called_with("Game over")
                    self.assertEqual(self.game.turns, 10)

    # def test_game_logic(self):
    #     with patch('builtins.input', return_value=10):
    #         with patch.object(self.game, '_print') as mock:
    #             guess = self.game.game_logic(50)
    #             mock.assert_called_with("Your guess is too low")

    # get_input will return 'yes' during this test
    # @patch('guessgame.guessanumber.get_user_input', return_value='1')
    # def test_get_user_input_1(self, input):
    #     self.assertEqual(answer(), 'you entered 1')

    # @patch('yourmodule.get_input', return_value='no')
    # def test_answer_no(self, input):
    #     self.assertEqual(answer(), 'you entered no')