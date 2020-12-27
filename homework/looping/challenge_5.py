"""
Write a program that asks the user to enter a starting number (integer), ending number (integer), and the word "even" or
"odd". Then generate a customized printout on their input. Here's a sample run of the program:

Starting number: 5
Ending number: 15
Even or odd? even

6
8
10
12
14
"""


EVEN = "even"
ODD = "odd"


def get_start_and_end():
    """
    asks the user to enter a starting number (integer), ending number (integer)
    :return: start: int, end: int
    """
    while True:
        try:
            start = int(input("start int: "))
            end = int(input("end int: "))
            break
        except ValueError:
            print("you did not enter proper ints. try again...")
    return start, end


def get_parity():
    parity = input(f"{EVEN} or {ODD} ")
    # while parity != ODD and parity != EVEN:
    while parity not in [ODD, EVEN]:
        print("thats not a proper parity, try again")
        parity = input(f"{EVEN} or {ODD} ")
    return parity


# def determine_parity(start, end, parity):
#     if parity == "odd":
#         remainder = 1
#     else:
#         remainder = 0
#     for num in range(start, end + 1):
#         if num % 2 == remainder:
#             print(num)


def determine_parity_better(start, end, parity):
    if parity == ODD and start % 2 == 0:
        start += 1
    elif start % 2 == 1:
        start += 1
    for num in range(start, end + 1, 2):
        print(num)


def main():
    start, end = get_start_and_end()
    parity = get_parity()
    determine_parity_better(start, end, parity)


main()
