"""
for loops revisited:
lets try to iterate on some more lists
"""

# fruits = ["apples", "plums", "oranges", "lemons", "grapefruits", "limes", "bananas"]
#
# for fruit in fruits:
#     print("did you know")
#     if fruit == "apples":
#         print("\tthere are ~7,500 varieties of apples in the world")
#     elif fruit == "plums":
#         print("\tprunes are just dried plums")
#     elif fruit ==  "bananas":
#         print("\tbananas have the most potassium")
#     else:
#         print(f"\t{fruit} are considered a citrus fruit")


"""
nested loops:
you can have multiple loops within each other

example:
    iterate over years and months in those years
"""

for year in range(2015, 2017):
    # print(f"the year is now {year}")
    for month in range(1, 13):
        # print(f"\tmonth #{month}")
        print(f"{month}/{year}")
    print()