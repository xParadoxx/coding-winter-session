"""
Write a simple "shopping cart" program that asks the user for a series of product prices.
Compute sales tax (7%) on each price and print out the new price to the user.
Next, ask the user if they want to enter another price - if they do, repeat the process.

If not, end the program.

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

"""

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
    response = input("wanna do checkout? [yes or no] ")
    while response == "yes":
        item, price = get_item_and_price()
        tax, total = calc_tax_and_total(price)
        print(f"for item: {item} \n\t--> tax: ${tax:.2f}\n\t--> total: ${total:.2f}")
        response = input("enter another item and price? [yes or no] ")

    print("okay have a nice day!!!")


main()
