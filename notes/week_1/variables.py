"""
this is called the docstring of the file / application
it is supposed to represent what is done in this program

Variables:

variables in python hold different values. this means that they have some sort of Type

some types (builtin):

int --> integer
bool --> boolean (true or false)
float --> floating point (basically a decimal)
double --> decimal (also the same thing as a floating point)
str --> string (of text)

NOTE:
    1) double is more precise than float (1/3 --> 0.333333...)
    2) language is made up of characters, and a string of characters makes up words, and strings of words make up
        sentences --> string is just text

RULES:
--> variables are case sensitive
--> they must contain letters, numbers, and underscores ONLY
    ex:
    x = 10  # GOOD
    !xXBadassXx! = 10  # BAD
--> they cannot contain special characters
--> they cannot contain spaces
--> they should (basically, must) have meaningful names. ignore examples that I use when we program

Example 1: tip calculator

GOOD NAMES:
total_amount = 330.45
tip = 21

BAD NAMES:
x = 330.45
y = 21

COMPARE TO C-STYLE:
double total_amount = 330.45; --> total_amount = 330.45

Example 2: video games

GOOD NAMES:
velocity = 12.8  # float
damage = 10  # int
hp = 6000  # int

BAD NAMES:
x = 12.8
y = 10
z = 6000

L-VAL vs. R-VAL

L-val is the value on the lhs of the equal sign.
R-val is the value on the rhs of the equal sign.

The equal sign is called the assignment operator (never say equal sign again).
this is NOT equality, it is assignment

it means the variable on the lhs will HOLD the value determined on the rhs.

IN MATH:

x = 7 // 7 = x

Ex:

x = 10
# here the value of x is 10
x = x + 1  # in math, this is a fallacy --> 0 = 1

in python, we execute the instructions from the top of the file to the bottom of the file. Line 73 occurs before
line 75.

in line 72, there is no variable called x.
after line 73, x holds the value of 10.
starting before line 75, x holds the value of 10.

when line 75 starts, the rhs gets executed first. so x holds the value of 10 still. the value of the rhs is 11.
so then x gets REASSIGNED to the value of 11.

so in line 76, x holds the value of 11.

that is why r-val occurs BEFORE l-val.

"""

x = 10
y = 15

z = x + y
# print(z)

z = 18
z += 1  # it's better than z = z + 1
# ++z and z++ do not exist

z = (x + y) + z  # 10 + 15 + 19
z += x + y

# PEMDAS --> precedence

# z = x + y * (x - y) / z

print(z)

"""
NOTE: some operators to care for:

+   --> addition
-
*
/   --> floating point division
//  --> integer division
%   --> modulo arithmetic: 9 % 4 --> 9mod4 --> 9 / 4 but you want the remainder: 1
  
"""

