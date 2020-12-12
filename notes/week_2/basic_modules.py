"""
so in python so far, we have been able to use the core set of functions that we have freely available:

print, input, type, etc...

however, there are times when we will want to access more "specialized" functions: think of sine and cosine and tangent!

thankfully, python supports the ability to import specialized functions from elsewhere. these are called modules

a module (also called a library, package, dependency, etc...) is a python file (or set of files) that contains code that
has some level of functionality that you want to use

so why do we care about modules? because we don't need to define the sine function ourselves -- we just need to use it!

and in order to use it, we need to bring the features (functions and variables and everything else they have)
into our program
"""

"""
one example module we want to use is the math module

we bring the functions and variables and features in that module into our program by using an import statement
"""


import numpy

# import math  # asks python to give us access to all of the functions in the "math" module
from math import sin, pi, e, radians


# now run the "sin" function defined inside the math module
# we first have to tell python to look inside of the "math" module to find the definition of the sin function
# we use the "dot" operator / character followed by the name of the feature we want to access

# print(f"sin of pi (inaccurate) is {math.sin(3.1415)}")
#
# # BETTER:
# print(f"sin of pi (accurate) is {math.sin(math.pi)}")
#
# print(f"this is pi {math.pi}")
# print(f"this is euler's number e {math.e}")
#
# # some more examples:
# print(f"sin of 90 degrees: {math.sin(math.radians(90))}")

print(f"sin of pi (inaccurate) is {sin(3.1415)}")

# BETTER:
print(f"sin of pi (accurate) is {sin(pi)}")

print(f"this is pi {pi}")
print(f"this is euler's number e {e}")

# some more examples:
print(f"sin of 90 degrees: {sin(radians(90))}")
