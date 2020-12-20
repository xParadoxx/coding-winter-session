"""
Write a program that plays a simple coin flip game with the user.

NOTE:
    instead of using strings, we can ONLY use ints
"""

from random import randint


HEADS = 1
TAILS = 2


def get_user_move():
    try:
        return int(input(f"press 1 for heads or 2 for tails? "))
    except ValueError:
        return 0


def coin_flip():
    return randint(1, 2)


def main():
    user_move = get_user_move()
    # if user_move != HEADS and user_move != TAILS:
    if user_move not in [HEADS, TAILS]:
        print("that's not a possibility")
        return
    coin_toss = coin_flip()
    # OPTIONAL
    string_user_move = "heads" if user_move == HEADS else "tails"
    string_flip_move = "heads" if coin_toss == HEADS else "tails"
    print(f"your move was {string_user_move} and the flip was {string_flip_move}")
    if user_move == coin_toss:
        print("you got it!!")
    else:
        print("better luck next time")


main()
