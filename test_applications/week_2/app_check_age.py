"""
Write a fully-functioning program (with a main function) that gets the user's name and age
if they are above the age of 18, they get drafted into the army
if they are or below the age of 18, they stay in school

NOTE: if the user gives an invalid age, make sure to print out a warning message.
"""


def get_name_and_age():
    name = input("whats your name bruh? ")
    age = int(input("how old are you? "))
    return name, age  # these two variables are local to the function get_name_and_age


def classify_user(name, age):
    if age > 18:
        print(f"hey {name}, straight to the army for you!")
    # elif 0 < age and age <= 18:
    elif 0 < age <= 18:
        print(f"so {name}, you need to stay in school because its cool")
    else:
        print(f"{name}, are you a real human? that's not a real age!!!!")
    return


def main():
    print("hi welcome to this weird program where i ask for your name and age and classify you!")
    user_name, user_age = get_name_and_age()
    # classify_user(name=user_name, age=user_age)
    classify_user(user_name, user_age)


main()
