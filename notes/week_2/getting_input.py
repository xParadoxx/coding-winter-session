"""
this whole time we are using information that we have previously known in our application --> completely self-contained
but how do we get information to come into our application

one method is to get it from the user of our program (as text)
"""

"""
in order to get input from the user, we need a way to connect the keyboard of the user to our program as an input stream

i want text --> we use a built-in function called input()
"""


# user_input = input("what do you wanna pass into your program? ")
# print(f"you passed in {user_input}")


"""
it is very critical to note that what the input function returns is always going to be a string. ALWAYS --> str
"""


# user_age_str = input("how old are you chief? ")
# user_age = int(user_age_str)
# user_age = int(input("how old are you chief? "))

"""
it doesn't make logical sense for us to get a string back from someone regarding their age
"""

# maturity_level = user_age - 50
# print(f"your maturity level is {maturity_level}")

"""
fix: cast whatever the input is to an int aka change the type from a str to int
"""

# user_age = int(input("seriously though bruh how old are? "))  # you're at the mercy of the user

"""
OPTIONAL:
--> branching statement with an if - elif - else
        a bit more all over the place
        its better to take this route
--> exception / error handling will take care of it for you
        cleaner, better looking code
        it is incredibly slow in terms of performance
"""

# try:
#     user_age = int(input("seriously though bruh how old are? "))  # you're at the mercy of the user
# except ValueError:
#     print("that's not a proper age value")

