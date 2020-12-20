"""
Write a program that plays a simple coin flip game with the user.

NOTE:
    "  heads" != "heads"
    "HEADS" != "heads"
    global variables are defined at the import level; they are always in all caps, and represent constant, unchanging
        values
"""

from random import randint


HEADS = "heads"
TAILS = "tails"


def get_user_move():
    move = input(f"{HEADS} or {TAILS}? ")
    return move.strip().lower()


def coin_flip():
    # 1 --> heads, 2 --> tails
    move_value = randint(1, 2)
    if move_value == 1:
        return HEADS
    else:
        return TAILS


def main():
    user_move = get_user_move()
    if user_move != HEADS and user_move != TAILS:
        print("that's not a possibility")
        return
    coin_toss = coin_flip()
    print(f"your move was {user_move} and the flip was {coin_toss}")
    if user_move == coin_toss:
        print("you got it!!")
    else:
        print("better luck next time")


main()
