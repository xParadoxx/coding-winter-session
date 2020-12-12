"""
some examples of functions that simply perform tasks:
"""

# only a function definition
def display_my_name():
    print("hi my name is slim shady")


# we also need the function call:
# display_my_name()
# display_my_name()
# display_my_name()


def display_name(given_name):
    # print(f"nice to meet you {given_name}")
    print("nice to meet you {}".format(given_name))


# display_name("little pump")


def display_name_and_age(name, age):
    print(f"hi my name is {name} and i am {age} years old")
    # print("hi my name is {} and i am {} years old".format(name, age))


# my_variable = display_name_and_age("grandpa joe", 17)

# print("ABCD"*20)
# print(f"this is my variable: {my_variable}")


"""
defining functions that return specific values:
"""


def f(x):  # defining f
    y = 2 * x + 4

# my_val = f(2)  # calling f and passing in 2
# print(f"what is my_val? {my_val}")  # None


def better_f(x):
    y = 2 * x + 4
    return y


# better_my_val = better_f(2)
# print(f"what is better_my_val? {better_my_val}")


"""
define a function of the form:
g(x, y) = 3x - 7y + xy
"""


def g(x, y):
    return 3 * x - 7 * y + x * y


some_value = g(0, 1)

print(f"some_value = {some_value}")  # should return -7


