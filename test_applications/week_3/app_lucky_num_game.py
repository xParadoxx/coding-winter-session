"""
Write a program where the user guesses a random integer from 1 to 10.
If the user picks the right number, they win a PS10 (2 PS5s).
If the user picks the wrong number, they go to gulag.
"""

import random


def get_user_guess():
    return int(input("whats your lucky number from 1 to 10: "))


def get_winning_num():
    return random.randint(1, 10)


def main():
    guess = get_user_guess()
    lucky = get_winning_num()
    print(f"DEBUGGING: the lucky number was {lucky}")
    if guess == lucky:
        print("here are your two ps5s aka ps10")
    else:
        print("str8 to the gulag")


main()
