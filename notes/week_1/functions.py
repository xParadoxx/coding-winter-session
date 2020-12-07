"""
the purpose of this lesson is to learn about functions

functions are of two forms (more than two but we will consider only two): built-in and user-defined functions

built-in: (provided by the system - python)
examples:
--> print()
--> type()

in math: a function is a relation in which for every input, there is always a unique output

in code:
    a function is a relation in which 0 or more inputs perform a specific action, and 0 or more outputs (of the
    function) may be given
    as long as an action is performed (i.e. functionality), the function serves its purpose
    any task that must be done should be done in a function
    MAIN ADV: code reuse

RULES:
--> the rules of naming functions is EXACTLY the same way as the rules of variables (identifier or names --> namespace)
--> there are some other things to consider when dealing with functions, which we will deal with later

SKELETON:

def function_name(parameter1, parameter2, ...):
    ... this is where the code to the function goes ...

NOTES:

--> there are two parts of any function:
1) defining a function: telling the system what the function does // function definition
2) calling a function: using the function itself // function call
"""

"""
for built-in functions, the definition is already in the python environment i.e. the system already knows what that
    function does
all we need to do is use it (call it) 
"""

"""
functions in math:
ex 1:
f(x) = 2x + 4 // a linear function --> a line
  ^
that x is called the parameter / argument of the function --> it's anything you pass into it

f(2) = 2 * 2 + 4 = 8
f(-5) = 2 * (-5) + 4 = -6

ex 2:
f(x, y) = 3x - 7y + xy // a multivariable function that defines a surface (non-convex)
    ==> x and y are called parameters, f is the name of the function

f(0, 1) : 3 * 0 - 7 * 1 + 0 * 1 = -7
f(1, 1) : 3 * 1 - 7 * 1 + 1 * 1 = -3

z = f(1, 1)
z holds the value of -3

IN CODE:
a function can have zero or more parameters
a function does not NEED to output / return anything back to you
"""

# print("check this line out")
# print()
# print("here", 17)

# x = 16
# print(x)
# print("here is\n")  # \n --> newline character

# z = 16.
# print("my variable z holds the value of", z)
# print("my variable z holds the value of %s" % z)
# print("my variable z holds the value of {}".format(z))
# print(f"my variable z holds the value of {z}")

"""
the type function is a built-in function that returns the type of the variable passed in
"""

# x = 14
# type_of_x = type(x)
# print(type(x))
# my_string = "this is an example of a string"
# print(type(my_string))

# is_smart = False  # True and False are keywords --> they hold a boolean
# print(f"am i really smart? {is_smart}")
# print(f"whats the type of smart? {type(is_smart)}")

"""
TAKEAWAYS:
--> keywords cannot be used as variable names
--> how the print function works
--> how the type function works
"""

# print(f"what happening here? {type()}")  # type function NEEDS either 1 argument or 3 arguments

"""
USER DEFINED FUNCTIONS:
"""

# from line 109 to 116 is a part of the function of random_function
def random_function(argument1: int, argument2: int):
    # this line
    # this line
    # and even this line
    # are all a part of the function definition of the function random_function
    x = 15
    y = 17
    print("i am inside random_function and i am getting called")

# if i want to call the random_function, i need to use its name and pass in any required arguments
# random_function(20, 21)
# random_function()  # TypeError

"""
not all functions must return something:
recall:
- print function doesn't return anything, it simply outputs to the screen (this is the "task" that it performs)
- type does return something, it returns what the type of the variable passed in as an argument is

how do we return something: using the return keyword
"""

