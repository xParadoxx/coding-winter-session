"""
Write a program that asks the user for a rock-paper-scissor move and then plays the user.

The program should RANDOMLY select a move, and output who won (or a draw).
"""


from random import randint

ROCK = 1
PAPER = 2
SCISSOR = 3


def get_user_move():
    try:
        return int(input(f"press 1 for rock, 2 for paper, and 3 for scissor? "))
    except ValueError:
        return 0


def get_computer_move():
    return randint(1, 3)


def play_game(user_move, computer_move):
    if user_move == computer_move:
        print("DRAW!!!!")
    elif (user_move == ROCK and computer_move == SCISSOR) or (user_move == PAPER and computer_move == ROCK) or \
            (user_move == SCISSOR and computer_move == PAPER):
        print("you win i guess :(")
    else:
        print("YOU LOSE!!!!")


def main():
    user_move = get_user_move()
    # validate the user move
    if user_move != ROCK and user_move != PAPER and user_move != SCISSOR:
        print("bruh you gotta pick a right move")
        return
    # now lets get the computer move
    computer_move = get_computer_move()
    print(f"your move is {user_move} and my move is {computer_move}")
    play_game(user_move, computer_move)


main()
