"""
Write a program that generates a random die roll on a six sided die. What about an n-sided die for n as any integer?
"""

from random import randint


def main():
    print(f"your die roll is: {randint(1, 6)}")


main()
