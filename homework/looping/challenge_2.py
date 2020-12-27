"""
Modify Challenge #1 so that your program also keeps track of the total amount spent in addition to total tax due.

Here's some sample output:

Enter an item price: 1.00
Tax on this item is 0.07 ; total price: 1.07
Enter another price? (yes or no): yes
Enter an item price: 2.00
Tax on this item is 0.14 ; total price: 2.14
Enter another price? (yes or no): yes
Enter an item price: 3.00
Tax on this item is 0.21 ; total price: 3.21
Enter another price? (yes or no): no
-------
Total amount due: 6.42
Total tax due: 0.42

"""

# OPTIONAL: set logging instead of printing
# import logging
# logging.basicConfig(level=logging.INFO)
# logging.info()
# logging.warning()
# logging.error()

SALES_TAX = 0.07


def get_item_and_price():
    item = input("what did you buy? ")
    price = float(input("how much was it? $"))
    return item, price


def calc_tax_and_total(price):
    tax = price * SALES_TAX
    total = price + tax
    return tax, total


def main():
    tax_total = 0  # accumulating the total tax
    price_total = 0
    response = input("wanna do checkout? [yes or no] ")
    while response == "yes":
        item, price = get_item_and_price()
        item_tax, item_total = calc_tax_and_total(price)
        tax_total += item_tax
        price_total += item_total
        print(f"for item: {item} \n\t--> tax: ${item_tax:.2f}\n\t--> total: ${item_total:.2f}")
        response = input("enter another item and price? [yes or no] ")

    print("-" * 10)
    print(f"TOTAL TAX: ${tax_total:.2f}\nTOTAL AMOUNT: ${price_total:.2f}")
    print("okay have a nice day!!!")


main()

