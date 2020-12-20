"""
Define a fully-functioning program (with a main function) that asks for the user's name, age, and favorite food
and responds with a greeting that includes their name, age, and fav food

example output:
"Hello Danny! I would imagine that I also like escargot at the age of 43!"

"""


def get_user_name():
    return input("whats your name? ")


def get_user_age():
    return int(input("how old are you? "))


def get_fav_food():
    return input("whats your fav food? ")


def main():
    print("hello, i have a few questions for you:")
    name = get_user_name()
    age = get_user_age()
    fav_food = get_fav_food()
    print(f"nice to meet you {name}. you're pretty old considering how you're {age}")
    print(f"and your taste in food is pretty mediocre at best because you like {fav_food}")


main()
