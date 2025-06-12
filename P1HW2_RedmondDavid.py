# David Redmond
# 12 June 2025
# P1 HW2
# Purpose is to accept integers, perform arithmetic and output a statement in the console when run.


def main():
    print("----This program calculates and displays travel expenses----\n")
    print("NOTICE: You may only use base numbers for any amounts.\n")

    budget = int(input("Please enter your budget: "))
    dest = input("Enter your travel destination. Which city are you visiting?: ")
    gas_expense = int(input("How much do you plan to spend on gas?: "))
    hotel_expense = int(input("How much will you spend on lodging?: "))
    food_expense = int(input("How much do you need for food?: "))
    # total_expense = gas_expense + hotel_expense + food_expense
    leftover = budget - (gas_expense + hotel_expense + food_expense)

    print("--------Travel Expense--------\n")

    print("Location:", dest)
    print("Initial Budget:", budget)
    print("\n")
    print("Fuel:", gas_expense)
    print("Accomodations:", hotel_expense)
    print("Food:", food_expense)
    print("\n")
    print("Remaining Balance:", leftover)


if __name__ == "__main__":
    main()
