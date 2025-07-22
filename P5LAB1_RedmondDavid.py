# David Redmond
# 14 July 2025
# P5 LAB1
# Purpose: to calculate change using a previous lab converted into a function.
# Notes: I put the disperse_change() code in a seperate file to be organized.
# I also used the round function for rounding instead of converting the dollars into cents.

import random
from class_utils import disperse_change


def main():
    amount_charged = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_charged} \n")

    while True:
        customer_payment = float(
            input("How much cash will you put in the self-checkout?: ")
        )
        if amount_charged > customer_payment:
            print("You did not enter enough total cash..")
            continue
        else:
            break

    change = round(customer_payment, 2) - round(amount_charged, 2)
    print(f"Change is: ${round(change, 2)}")
    disperse_change(change)


if __name__ == "__main__":
    main()
