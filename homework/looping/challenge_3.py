"""
Write a program that takes in as input a list of positive numbers. Note, you pass in the numbers one by one, and one by
one, they should be added to your list (or processed in some way).

After that, find the min and the max of the numbers in your list.

NOTE:
    1: one design choice: you can have the user tell you BEFOREHAND how many numbers he / she will input for your list.
    2: do NOT use the sort or the reverse method
    3: do NOT use the min / max functions
"""


def get_number_of_inputs():
    # try:
    #     return int(input("how many numbers are you going to input? "))
    # except ValueError:
    #     return -1
    num_input = input("how many numbers are you going to input? ")
    while not num_input.isdigit():
        print("not a valid number!")
        num_input = input("try again: ")
    # valid string
    return int(num_input)


def get_list_from_user(num_input):
    input_list = []
    while len(input_list) < num_input:
        possible_value = input("enter a value: ")
        if not possible_value.isnumeric():
            print("that is not valid input. try again")
            continue
        input_list.append(int(possible_value))
    # GOOD DESIGN (but overkill):
        # try:
        #     possible_value = int(input("enter a value: "))
        #     input_list.append(possible_value)
        # except ValueError:
        #     print("that is not valid input. try again")
        #     continue
    # BAD DESIGN
    # for i in range(num_input):
    #     try:
    #         val = int(input("enter a value: "))
    #     except ValueError:
    #         continue
    #     input_list.append(val)
    return input_list


def display_min_max(arr: list) -> None:
    """
    we find the min and the max of the arr without sorting or using max() or min() functions
    display it to stdout
    :param arr: input list from the user
    :return: None
    """
    # if arr == []:
    # if not arr:
    if len(arr) == 0:
        return
    largest_number = smallest_number = arr[0]
    for number in arr:
        if number > largest_number:
            largest_number = number
        elif number < smallest_number:
            smallest_number = number

    print(f"largest num {largest_number}")
    print(f"smallest num {smallest_number}")
    return


def main():
    num_input = get_number_of_inputs()
    input_list = get_list_from_user(num_input)
    # string_list = " ".join([str(x) for x in input_list])  # OPTIONAL
    # string_list = ", ".join(map(str, input_list))  # OPTIONAL
    # print(f"the input list you passed in is {string_list}")  # OPTIONAL
    print(f"the input list you passed in is {input_list}")
    display_min_max(input_list)


main()
