"""
LISTS (basics)

a list is a collection object of anything (in python)

to create a list, we have a set of brackets: []
we can put any number of items in our list, and we separate them by commas
a list IS ordered, so it matters which item comes first
"""

from math import pi

# a_list = [1, 2, -3, 4, 5.5]
# print(a_list)
# b_list = ["string 1", -12, "string 3", 0.256, pi]
# print(b_list)

"""
in order to access specific items in a list, we need to index through it. the index is the position of the list, where
if our list is of length n, the initial position is index 0 and the final position is index n-1

to index, we also use the bracket symbol (called the access / index operator) 
"""

# print(f"index 2 (3rd element): {b_list[2]}")
# print(f"index 4 (5th element): {b_list[4]}")

"""
how do we know how many elements are in a specific list?

to get the size of a list, you can use a builtin function called len()
"""

# print(f"my list is of size: {len(b_list)}")

"""
the range function is a builtin special function that technically creates a list for us

it creates a list of numbers, as a half opened range:

range(start, stop, step):
    [start, start + step, start + 2 * step, ...]
    the last number is start + n * step < stop
    the default of step is 1; the default of start is 0
    in math, this is called arithmetic sequence

NOTE: every time you use a range() function call outside of a loop, wrap it around:
list(range())

OPTIONAL:
range produces a generator --> an efficient way of having a list
a_list = list(range(100000000000000))  # [0, ..., 100000000000000 - 1] ; we don't want this flooding our ram
so we use a generator for it to only store 1 number at a time --> iterator  
"""

# print(list(range(5)))
# print(list(range(10)))

# a_list = list(range(10))  # missing start and step
# b_list = list(range(-10, 10))  # missing step
# c_list = list(range(-10, 10, 2))

# print(a_list, len(a_list))
# print(b_list, len(b_list))
# print(c_list, len(c_list))


"""
list slicing:
"""


# a_list = [1, -9, 15, 256, 420, 69]

# print(a_list[0 : 3])  # this is also a half-open range
# print(a_list[: 3])  # you can omit the zero if you want
# print(a_list[: 3: 2])  # two is your step
# print(a_list[: : 2])  # from beginning to end with a step of 2
# print(a_list[-1])  # last element in the list


"""
list operations / methods --> an operation you can perform on a list
"""

a_list = [1, -9, 15, 256, 420, 69]

# what if you want to add something to your list?

# a_list.append(1800)
# print(a_list)

b_list = [3.14, 2.718, 1.616]

print("combining two lists")
# a_list.extend(b_list)
# print(a_list)

""" a different way of combining lists (without changing the original ones): """

# c_list = a_list + b_list

# print(f"a: {a_list}")
# print(f"b: {b_list}")
# print(f"c: {c_list}")

a_list.append(b_list)
print(f"this is never something we want: {a_list}")
print(f"the last element is: {a_list[-1]}")
