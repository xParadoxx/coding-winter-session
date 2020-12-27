"""
Write a program that asks the user what the start and end integers are, then it finds the sum of all integers between
start and end, inclusive.
"""


def get_start_and_end():
    start = int(input("start int: "))
    end = int(input("end int: "))
    return start, end


def get_sum_1(start, end):
    value_list = list(range(start, end + 1))
    return sum(value_list)


def get_sum_2(start, end):
    pairs = (end - start + 1) / 2
    return pairs * (start + end)


def main():
    start, end = get_start_and_end()
    print(f"the sum of ints from {start} to {end} is {get_sum_1(start, end)}")


main()

