"""
MOTIVATION:
    you ever catch yourself needing to repeat something over and over again to someone or something?
    do you wish you can just run it on repeat and move?
    ever find yourself thinking that you want to run something over and over again in code?

when writing an application, you often find the need to repeat certain statements over and over again

EXAMPLE:
say you wanted to write a program to compute the tip on a restaurant bill
some sample code would be:

bill = float(input("enter your bill amount: $"))
rate = float(input("enter your rate (i.e. 0.15): "))
# calculate tip
print(f"your tip: {bill * rate}")

but what if you wanted to repeat this for 3 restaurant bills?

right now, you only know how to do this by copy / pasting:

bill = float(input("enter your bill amount: $"))
rate = float(input("enter your rate (i.e. 0.15): "))
# calculate tip
print(f"your tip: {bill * rate}")

bill = float(input("enter your bill amount: $"))
rate = float(input("enter your rate (i.e. 0.15): "))
# calculate tip
print(f"your tip: {bill * rate}")

bill = float(input("enter your bill amount: $"))
rate = float(input("enter your rate (i.e. 0.15): "))
# calculate tip
print(f"your tip: {bill * rate}")

SOME DISADVANTAGES TO THIS APPROACH:
--> what if you had to compute the bill for 1000 restaurant bills? this doesn't seem possible with this approach
--> very difficult to read + to maintain
    the likelihood of an error somewhere in your code is very high (even if you managed to copy/paste it somehow)

ONE SOLUTION:
take advantage of a programming technique called a "repetition structure": write your code one time and then place it
into a unique code block that runs it over and over again for however long you want
this is called a loop

2 kinds of loops:
while boolean-condition:
    print("this will continue to print over and over again")
    print("...as long as the condition above evaluates to True")

the trick here is to control the condition that is being evaluated --> one way to do this is to create a variable, which
can be used in any boolean expression (recall if statements)
"""

# while True:  # this loop is called an infinite loop
#     print("am i gonna eat up all of mo's ram?")
# print("yes i am probably!")

"""
the while loop is considered a pre-test loop, meaning that it only iterates upon successful evaluation of a condition
this means that you always need to "set up" your loop prior to python being able to work with it
"""

# set up a variable
x = 0

while x < 5:
    # add 1 to x - this is what we call a self-referential assignment aka self incrementing
    x += 1
    print(x)
    # now we go back to the condition on line 68
print("i am outside the loop")

"""
line 66: x is 0
line 8: we check x < 5 [True]
we go into the loop and do everything inside the loop:
    x is now 1
    we print 1
we go back to line 68, and we check x < 5 [True]
we go into the loop and do everything inside the loop:
    x is now 2
    we print 2
we go back to line 68, and we check x < 5 [True]
we go into the loop and do everything inside the loop:
    x is now 3
    we print 3
we go back to line 68, and we check x < 5 [True]
we go into the loop and do everything inside the loop:
    x is now 4
    we print 4
we go back to line 68, and we check x < 5 [True]
we go into the loop ad do everything inside the loop:
    x is no 5
    we print 5
we go back to line 68, and we check x < 5 [False]
we do not enter the loop and do not evaluate the loop body (in the loop) and we go to line 73
"""

