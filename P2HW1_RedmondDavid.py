# David Redmond
# 22 June 2025
# P2 HW1
# Purpose is to accept integers, perform arithmetic and output a statement in the console when run.


def main():
    print("----This program calculates and displays travel expenses----\n")
    print("NOTICE: You may use base numbers and decimals.\n")

    budget = float(input("Please enter your budget: "))
    dest = input("Enter your travel destination. Which city are you visiting?: ")
    gas_expense = float(input("How much do you plan to spend on gas?: "))
    hotel_expense = float(input("How much will you spend on lodging?: "))
    food_expense = float(input("How much do you need for food?: "))
    # total_expense = gas_expense + hotel_expense + food_expense
    leftover = budget - (gas_expense + hotel_expense + food_expense)

    print("--------Travel Expenses-----------------------\n")

    # :>{int} pads out the string.
    print(f"Location: {dest:>25}")
    print(f"Initial Budget: {'$':>7}{budget:.2f}")
    print(f"Fuel: {'$':>17}{gas_expense:.2f}")
    print(f"Accomodations: {'$':>8}{hotel_expense:.2f}")
    print(f"Food: {'$':>17}{food_expense:.2f}")
    print("---------------------------------------------\n")
    print(f"Remaining Balance: {'$':>4}{leftover:.2f}")


if __name__ == "__main__":
    main()
