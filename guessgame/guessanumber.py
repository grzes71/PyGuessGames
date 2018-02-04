"Guess a Number simple game."

class GuessANumber:
    def __init__(self, number_to_guess, turns=10):
        self.__number_to_guess = number_to_guess
        self.__turns = turns
    
    @property
    def number_to_guess(self):
        return self.__number_to_guess

    @property
    def turns(self):
        return self.__turns

    @turns.setter
    def turns(self, value):
        self.__turns = value

    def get_user_input(self):
        while True:
            try:
                return int(input("Enter an integer from 1 to 99: "))
            except ValueError:
                print('This is not a numeric value, try again!')

    def self.game_logic(self, guess):
        if guess < number_to_guess:
            print("Your guess is too low")
        elif guess > number_to_guess:
            print("Your guess is too high")
        else:
            print("You guessed it!")
            return True
        self.turns -= 1

    def play(self):
        number_to_guess = 50
        while self.turns:
            guess = self.get_user_input()
            if self.game_logic(guess):
                break
        else:
            print("Tries number exceeded, sorry!")
        print("Game over")


def main():
    guess_a_number()


if __name__ == '__main__':
    main()
