"""
recall last week we saw some basic while loops
"""

""" built in python debugger """
# import pdb

# set up a variable
""" used to set a breakpoint for the builtin debugger """
# pdb.set_trace()
x = 0

while x < 5:
    # add 1 to x - this is what we call a self-referential assignment aka self incrementing
    x += 1
    print(x)
    # now we go back to the condition on line 68
print("i am outside the loop")

"""
NOTE: self-referential
x = x + 1
shortcut:
x += 1
"""


"""
NOTE: loops
while loops are often used because they execute an indeterminate number of times
but you can also use while loops to execute for a set # of times (i.e. 5 times in the previous example)
the x is called the loop variable (a type of accumulator) 
"""

accum = 0 # define the accumulator variable
while accum < 10:
    print(f"hello! we are currently on {accum + 1}")
    # increase the accumulator by 1
    accum += 1

"""
GOOD DESIGN:

when setting up your while loop, don't set it up to succeed first, and then break out later on
make sure the condition is logical and that you're solving the right problem, not just an example
"""



