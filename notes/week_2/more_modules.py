"""
last class we talked about modules, what they are, and using them because they have code that performs tasks that we
might care about

we saw the math module last class, along with other useful modules such as numpy, pandas, etc.

there is also a module called the random module

random numbers are often used in computer programs to give your programs the ability to make their own "decisions"

real-life examples:
weapon drops / chest drops in games are randomized using some sort of a random-number generator (rng)

our example:
let's say you're writing a program to play a game of rock-paper-scissors with the user -- we could easily ask the user
which symbol they wanted to play, but how would the computer pick its symbol?

we could pick random numbers, and then map them to specific values ==> f(random_number) --> selected_move
"""

import random

# get a number between 1 and 3: it could be 1, 2, or 3 (the computer will "decide")
# random_num = random.randint(1, 3)
# print(f"your random number is {random_num}")


"""
in any given application, your import statements must be at the top of the program --> ALMOST ALWAYS
"""


"""
if you need a random floating point:
"""

random_floating_num = random.random()  # half open range from [0.0, 1.0) --> [0.0, 3.0) OR [0.0, 10.0) OR [0.0, 37.0)
print(f"your random number is {100 * random_floating_num}")

"""
RECALL: other ways to import modules:

--> import MODULE_NAME
    ex: import random

--> from MODULE_NAME import *  # the * is called a wildcard
    ex: from math import *

OPTIONAL (for now):
--> import MODULE_NAME as ANOTHER_NAME
    ex: import math as m
    ex: import numpy as np
    ex: import pandas as pd
"""

