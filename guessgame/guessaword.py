
class GuessAWordGame:
    "Guess a word game class."
    def __init__(self, word, tries=10, name='John Doe'):
        self.word = word.upper()
        self.tries = tries
        self.guesses = []
        self.name = name

    def generate_word_to_display(self):
        return ''.join(char.upper() if char in self.guesses else '*' for char in self.word)

    def display_word(self):
        word = self.generate_word_to_display()
        print("\n", word, '\n', '=' * len(self.word), sep='')

    def game_logic(self, guess):
        if guess and len(guess)==1 and guess in self.word:
            print("You've guessed it!")
            self.guesses.append(guess)
            if set(self.guesses) == set(self.word):
                return True
        else:
            self.tries -= 1
            print("Wrong! You have {} tries left, {} ...".format(self.tries, self.name))

    def play(self):
        while self.tries > 0:
            self.display_word()
            guess = input("\nGuess a character: ")
            guess = guess.upper()
            if self.game_logic(guess):
                self.display_word()
                print("Congratulations {}!".format(self.name))
                break
        else:
            print("Tries number exceeded, sorry!")
        print("Game over")

def get_user_name(gamename):
    username = input("What is your name? ")
    print("Hello {}, time to play {} game!".format(gamename, username))
    return username

def main():
    name = get_user_name('Guess a Word')
    game = GuessAWordGame('secret', name=name)
    game.play()

if __name__ == '__main__':
    main()