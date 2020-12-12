"""
so far we have discussed statements, variables, types, and functions

today, we will be looking into discussing boolean operations

a field of math called discrete math --> goes into details on boolean operators and operations

two values for booleans: True and False

basic logical operators:

== --> equals
!= --> not equals
<  --> less than
>= --> greater than or equals
>  --> greater than
<= --> less than or equal to

Examples:
    1) 3 == 4   [False]
    2) 3 <= 3   [True]
    3) 17 != 17 [False]
"""

# will_the_world_end = 3 == 3  # True
# print(f"will the world end bro? {will_the_world_end}")


"""
more complicated logical expressions:

more operators

and --> logical and
or  --> logical or
not --> logical not

for AND: # everything must be True for the entire expression to be True

True and False  --> False
False and True  --> False
False and False --> False
True and True   --> True

for OR: # only one expression must be True for the entire expression to be True

True or False   --> True 
False or True   --> True
False or False  --> False
True or True    --> True

for NOT: # negation of whatever the truth value is
not True    --> False
not False   --> True
    NOTE: no difference between not and ! (from C-style and JVM langs)


OPTIONAL:
short-circuiting is what python (and most other languages) do when evaluating logical expressions
--> if one sub expression of a chain of ors is True, then all other sub expressions are not evaluated
--> if one sub expression of a chain of ands is False, then all other sub expressions are not evaluated

"""


# is_coding_fun = (3 != 5) or (9 > 19)  # --> True or False --> True
# print(f"is coding fun tho... {is_coding_fun}")

another_boolean = (19 >= -10) and (17 < 5)  # True and False --> False
print(not another_boolean)  # not False --> True


"""
the following lines are equivalent:

line 1: x - 1 >= 2 and y * 3 <= 4
line 2: ((x - 1) > 2) and ((y * 3) <= 4)
"""
