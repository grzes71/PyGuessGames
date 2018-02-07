from unittest.mock import patch
from unittest import TestCase, main

from guessgames.guessanumber import GuessANumber

class TestGuessaNumber(TestCase):

    def setUp(self):
        self.game = GuessANumber(50, 10)

    def test_turns(self):
        self.assertEqual(self.game.turns, 10)

    def test_number_to_guess(self):
        self.assertEqual(self.game.number_to_guess, 50)

    def test_gamename(self):
        self.assertEqual(self.game.gamename, 'Guess A Number')

    def test_get_user_int(self):
        with patch('builtins.input', return_value=10):
            guess = self.game.get_user_int("Enter an integer from 1 to 99: ")
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
                mock.assert_called_with("You guessed it Unknown!")
                self.assertEqual(self.game.turns, 10)

    def test_play_game_loop_success(self):
        with patch.object(self.game, 'get_user_int', return_value=50):
            self.game.game_loop()
            self.assertEqual(self.game.turns, 10)

    def test_play_game_loop_failure(self):
        with patch.object(self.game, 'get_user_int', return_value=0):
            self.game.game_loop()
            self.assertEqual(self.game.turns, 0)

    def test_play_failure(self):
        with patch.object(self.game, '_input_name', return_value='steve'):
            with patch.object(self.game, 'get_user_int', return_value=0):
                self.game.play()
                self.assertEqual(self.game.turns, 0)

    def test_play_success(self):
        with patch.object(self.game, '_input_name', return_value='steve'):
            with patch.object(self.game, 'get_user_int', return_value=50):
                self.game.play()
                self.assertEqual(self.game.turns, 10)


if __name__ == '__main__':
    main()
