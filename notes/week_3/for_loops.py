"""
so far we have seen while loops in action, but are there any other types of loops?

there is: for loop

a for loop can iterate over any fixed set of items. those items can be as simple as a set of numbers, or as complex like
a series of strings or other data types

a for loop has the following syntax:

for loop_variable in list_of_items:
    ... execute certain statements ...

TRANSLATION:
in plain english, this reads as "for each loop_variable that exists in list_of_items, execute a certain set of
statements
"""

# count = 0
# while count < 5:
#     count += 1

# def say_hello_n_times(n):
#     for count in range(n):  # count is a loop variable - it only exists in the loop
#         print("hello")
#     # count does not exist anymore
#     """
#     C-Style Languages
#     for(int i = 0; ; i++) {
#     }
#     """
# say_hello_n_times(8)


# for count in range(5):
#     print(count)


"""
we can also loop through lists and each item in a list
"""


# top_nba_players = ["mj", "lebron", "kobe", "shad", "mailman", "pippen", "kd"]
# for player in top_nba_players:
#     print(f"current player name is: {player}")


# game_moves = ["rock", "paper", "scissor"]
#
# for move in game_moves:
#     print(move)


for i in [-10, 20, 30.5, 50, 40]:
    print(f"the value of i is {i}")


