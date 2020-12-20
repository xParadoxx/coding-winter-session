"""
write a program that asks the user for the price of an item they are purchasing. items are eligible for a discount based
no their price as follows:

$10 or less: no discount
between $10 and $50: 10% discount
over $50: 20% discount
Ensure that you don't allow the user to enter negative values or zero as a price value
OPTIONAL: include error handling in your code to avoid invalid input
"""


def get_original_price():
    original_price = float(input("what is the original price of your item: $"))
    return original_price


def apply_discount(original_price):
    if original_price <= 10:
        discount = 0
    elif 10 <= original_price <= 50:
        discount = 0.1
    else:
        discount = 0.2
    # total = original_price - discount * original_price
    total = (1 - discount) * original_price
    print(f"you received a discount percentage of {discount * 100}%")
    print(f"your total is ${total:.2f}")
    return


def main():
    orig_price = get_original_price()
    if 0 < orig_price:
        apply_discount(orig_price)
    else:
        print("error...please give a valid price")


main()
