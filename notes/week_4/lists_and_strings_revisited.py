"""
we looked at string methods and functionality
we also looked at string formatting (both c style, pythonic, and .format method)

strings can also be thought of as a list of single character strings
you can even get the number of characters in a string (aka the length) just like you did with lists
"""

# string = "this is my sample string. isnt it noiiiiiiiceeeee"

# print(string)
# print(f"my string is of size {len(string)}")

# print(len(""))
# print(len([]))

# print(string[:: 3])  # recall slicing

# print(string.upper() == string)


# a_list = ["first", "nineteenth", "twenty won"]
# b_list = [10, 3.14, 4.1415, -9, 467]

# for a in a_list:
#     print(a)

# for index in range(len(a_list)):
#     print(a_list[index])

"""
if you want to add a 1 to each element in b_list, then we need to loop over b_list
"""

# BAD
# for b in b_list:
#     b

# GOOD
# for i in range(len(b_list)):
#     b_list[i] += 1
#
# print(b_list)

# OPTIONAL 1: list-comprehension (shorthand of lines 37 and 38)
# new_list = [x + 1 for x in b_list]

# OPTIONAL 2: functions as first-class citizens
# PART A: defined function


# def add(x):
#     return x + 1
# new_list = list(map(add, b_list))
#
# print(new_list)

# PART B: anonymous function w/ the lambda keyword
# new_list = list(map(lambda x: x+1, b_list))

# print(new_list)


# ANOTHER EXAMPLE:
# string_b_list = list(map(str, b_list))
# print(string_b_list)

"""
in operator:

we can check to see if a specific element is in a list using the in op
"""

a_list = ["first", "nineteenth", "twenty won"]
b_list = [10, 3.14, 4.1415, -9, 467]

# if "first" in a_list:
#     print("im in there dude")
# else:
#     print("nope not in there")
#
# if "second" not in a_list:
#     print("its not there sir")


"""
recall on some useful list methods and useful things about them 
"""

# print(b_list)
# b_list.sort()
# print(b_list)
# b_list.reverse()
# print(b_list)

# print(a_list)
# a_list.sort()
# print(a_list)

# print(a_list.index("first"))
# if "second" in a_list:
#     print(a_list.index("second"))
# elif "nineteenth" in a_list:
#     print(a_list.index("nineteenth"))

# print(b_list)
# print(min(b_list))
# print(max(b_list))
# print(sum(b_list))

# print(a_list)
# print(min(a_list))
