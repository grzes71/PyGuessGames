import argparse 
import json
from random import randint, choice

from guessgames.guessanumber import main as play_guessanumber
from guessgames.guessaword import main as play_guessaword

def game_guessaword(arg):
    word = 'secret'
    if arg.word:
        word = arg.word
    else:
        if arg.config:
            with open(arg.config, 'r') as f:
                json_obj = json.load(f)
                word = choice(json_obj['words'])
    play_guessaword(word, 10)

def game_guessanumber(arg):
    play_guessanumber(arg.number, 10)

def main():
    par = argparse.ArgumentParser()
    sub = par.add_subparsers(help='Select game')
    pa1 = sub.add_parser('guessanumber', help='Guess a number')
    pa2 = sub.add_parser('guessaword', help='Guess a word')
    pa1.add_argument('--number', type=int, default=randint(0,100))
    pa1.set_defaults(func=game_guessanumber)
    pa2.set_defaults(func=game_guessaword)
    group = pa2.add_mutually_exclusive_group()
    group.add_argument('--config', help='path to config file')
    group.add_argument('--word', help='word to guess')
    arg = par.parse_args()

    if hasattr(arg, 'func'):
        arg.func(arg)
    else:
        par.print_help()

if __name__ == '__main__':
    main()