"""
write a program that asks the user for a number between 1 and 5 (inclusive). then report to the user the following:

if the number is even or odd
if the number is prime, composite, or neither (which number is neither...?)
ensure that the user enters a number between 1 and 5 (you can print an error message if they supply an invalid number).
OPTIONAL: include error handling in your code to avoid non-int input
"""


# import math
# math.gcd(a, b) --> if gcd(a, b) = 1, then a and b are co-prime


def get_num_from_user():
    # num = int(input("pick a number form 1 to 5 (inclusive): "))
    try:
        return int(input("pick a number form 1 to 5 (inclusive): "))
    except ValueError:
        return -1


def main():
    num = get_num_from_user()
    if 1 <= num <= 5:
        if num % 2 == 0:
            print("your number is even")
        else:
            print("your number is odd")
        # for prime numbers: num is 2 OR 3 OR 5
        # for composite numbers: num is 4
        # neither: num is 1
        # if num == 2 or num == 3 or num == 5:
        if num in [2, 3, 5]:
            print("your number is prime")
        elif num == 4:
            print("your number is composite")
        else:
            print("your number is neither")
    else:
        print("error...you were supposed to give a valid number")


main()
