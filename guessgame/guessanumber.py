

def guess_a_number():
    number_to_guess = 50
    turns = 5 
    while turns > 0:
        guess = int(input("Enter an integer from 1 to 99: "))
        if guess < number_to_guess:
            print("Your guess is too low")
        elif guess > number_to_guess:
            print("Your guess is too high")
        else:
            print("You guessed it!")
            break
        turns -= 1
    else:
        print("Tries number exceeded, sorry!")
    print("Game over")


def main():
    guess_a_number()


if __name__ == '__main__':
    main()
