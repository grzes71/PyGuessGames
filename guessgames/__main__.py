import argparse
import random

from .guessanumber import main as guess_a_number_game
from .guessaword import main as guess_a_word_game

def game_number(args):
    guess_a_number_game()

def game_word(args):
    guess_a_word_game()


def parse_args():
    parser = argparse.ArgumentParser(description='Guessing games')
    subparsers = parser.add_subparsers(title='games',
                                       description='select game to play',
                                       help='enter name of game to play')

    number_p = subparsers.add_parser('guessanumber', help="Guess a Number game")
    number_p.add_argument("--number", type=int, help="number to guess", default=random.randint(0, 100))
    number_p.add_argument('--tries', type=int, help='number of tries', default=10)
    number_p.set_defaults(func=game_number)

    word_p = subparsers.add_parser('guessaword', help="Guess a Word game")
    word_p.add_argument("word", help="word to guess")
    word_p.add_argument('--tries', type=int, help='number of tries', default=10)
    word_p.set_defaults(func=game_word)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)

if __name__=='__main__':
    main()