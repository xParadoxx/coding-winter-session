"""
Lucky num game, but more robust
"""

import random

LOWER_BOUND = 1
UPPER_BOUND = 10


def get_user_guess():
    return int(input("whats your lucky number from 1 to 10: "))


def get_winning_num():
    return random.randint(LOWER_BOUND, UPPER_BOUND)


def main():
    response = input("do wanna play a game? [yes or no] ").strip().lower()
    while response == "yes":
        guess = get_user_guess()
        lucky = get_winning_num()
        print(f"the lucky number was {lucky}")
        if guess == lucky:
            print("here are your two ps5s aka ps10")
        else:
            print("str8 to the gulag")
        response = input("do you wanna play again? [yes or no] ").strip().lower()
    # while True:
    #     guess = get_user_guess()
    #     lucky = get_winning_num()
    #     print(f"the lucky number was {lucky}")
    #     if guess == lucky:
    #         print("here are your two ps5s aka ps10")
    #     else:
    #         print("str8 to the gulag")



main()
