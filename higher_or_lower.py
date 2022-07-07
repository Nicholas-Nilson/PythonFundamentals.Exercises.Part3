from random import randrange


def user_guess():
    guess = int(input("please enter a number from 1 to 10\n"))
    while guess <= 0 or guess > 10:
        guess = int(input("please enter a number from 1 to 10\n"))
    return int(guess)


def random_number():
    return randrange(10)

def get_result(guess, random):
    if guess < random:
        print("Guess: " + str(guess) + ". Actual: " + str(random) + ". Your guess was too low")
    elif guess > random:
        print("Guess: " + str(guess) + ". Actual: " + str(random) + ". Your guess was too high")
    else:
        print("Your guess of: " + str(guess) + " was correct!")


get_result(user_guess(), random_number())
