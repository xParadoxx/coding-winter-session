"""
boolean logic is very much necessary in order to better understand how conditional statements work

but what are conditional statements?

conditional statements are also known as branching statements, and they evaluate a different block of code depending
on the boolean expression that is present (or evals to true rather)
NOTE: conditional statements are resolved top-down

format of the language:

if boolean-expr-1:
    ... do something ...
elif boolean-expr-2:
    ... do something else ...
...
else: # default case
    ... do the default case ...

the first if statement is required -- all other statements can be omitted

NOTE: conditional statements are mutually exclusive (disjoint) --> if one occurs, then the others do not

EXAMPLE 1:
--> coin flip

if heads:
    do whatever you need to do for heads
else:  # tails by default
    do what you need to do for tails

BAD DESIGN:

if heads:
    do whatever you need to do for heads
elif tails:  # we don't need to check for this; this is the default case
    do what you need to do for tails

EXAMPLE 2:
--> rock paper scissors game

if rock:
    do rock things
elif paper:
    do paper things
else:
    do scissor things

NOTE: illogical for this case

if rock:
    do rock
if paper:
    do paper
if scissor:
    do scissor

EXAMPLE 3:
--> lottery system
consider the following situation:
there is a lottery system in your county where we have prizes for various categories of winners:
1st --> 1 million pennies
2nd --> 2 million dollars
3rd --> ps5 box with a ps4 inside
4th --> a high five from the pope

if (you are the first place):
    get 1 million pennies
elif (you are second place):
    get 2 million dollars
elif (you are third place):
    get a ps5 box with a ps4 inside
elif (you are fourth place):
    get a high five from the pope


EXAMPLE 4:
birthday

if (your birthday):
    get a happy birthday

NOTE:
< and >= are opposite operators
< and <= are opposite operators
"""

x = 5
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
# elif x == 0:
else:
    print("x is zero")

"""
from lines 89 to 90 is the if block, but from lines 89-95 is the if-elif-else block)
"""

"""
DESIGN:

boolean variables should have names are predicates --> verb phrases
examples:
1) is_ugly
2) is_set
3) is_running
4) is_unit_test_passing

RECALL:
functions also have a naming structure --> they are also verb-like, but not predicates
1) def display_name():
2) def get_user_age():
3) def calculate_tip():

RECALL:
any other kind of variable should be noun-like ALWAYS:
examples:
1) tip
2) velocity
3) damage
4) name
"""




