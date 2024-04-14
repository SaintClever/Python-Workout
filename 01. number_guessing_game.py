from random import randint


def guessing_game():
    rand_int = randint(0, 100)
    user_input = int(input("Guess what number has been chosen: "))

    if user_input > rand_int:
        return "Too high"
    elif user_input < rand_int:
        return "Too low"
    return "Just right"


print(guessing_game())
