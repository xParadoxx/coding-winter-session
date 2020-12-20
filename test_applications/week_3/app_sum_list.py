"""
Write a program that iterates over a large set (from 1 to 10000) of numbers and compute a total running sum.

NOTE:
    1 + 2 + 3 + ... + N - 1 + N = N(N+1)/2
"""


def validate_sum(final_num):
    total = final_num * (final_num + 1) // 2
    return total


# def python_summation(a_list):
#     return sum(a_list)


def main():
    total = 0
    for i in range(10000 + 1):
        total += i
    print(f"the sum of all numbers from 1 to 10000 is \n\t{total}")
    print(f"the validated sum of all numbers from 1 to 10000 is \n\t{validate_sum(10000)}")
    print(f"validated from python \n\t{sum(list(range(10000 + 1)))}")


main()
