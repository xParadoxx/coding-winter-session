"""
Write a program that finds the multiples of 5 given a range of numbers.
"""


def get_endpoints():
    start = int(input("start number: "))
    end = int(input("end number: "))
    return start, end


def get_multiples(start, end):
    for num in range(start, end + 1):
        if num % 5 == 0:
            print(f"{num} is a multiple of 5")


def main():
    start, end = get_endpoints()
    get_multiples(start, end)


main()
