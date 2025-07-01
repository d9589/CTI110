# David Redmond
# 29 June 2025
# P3 LAB1
# Purpose is to take in a float and breakdown the amount into currentcy for dollars, quarters, dimes, etc.
# Note: # I'm bad at math so really going to break this down with excessive comments.


def main():
    # Take money as float.
    money = float(input("Enter the amount of money as a float: "))

    # Multiply by 100 to basically convert the whole dollar ammount into cents.
    total = money * 100

    # Convert to an int
    total = int(total)

    # Using floor to round. Using / would just give us back our float.
    # This also supports amounts less than 1.00.
    dollars = total // 100

    # Subtract the total amount of cents from the dollar amount in cents.
    # We do this because we basically want to only work with the total value as cents.
    cents = total - (dollars * 100)

    # We go in order of highest to lowest to calculate quarters, dimes, etc,
    # so we don't say 90 dimes instead of 3 quarters.
    # We use modulo to get the remainder and just step it down.

    quarters = cents // 25
    remain = cents % 25

    dimes = remain // 10
    remain = remain % 10

    nickels = remain // 5
    remain = remain % 5

    # We stop at pennies as it's the last amount.
    pennies = remain // 1

    if dollars > 0:
        print(f"{dollars} Dollars")
    if quarters > 0:
        print(f"{quarters} Quarters")
    if dimes > 0:
        print(f"{dimes} Dimes")
    if nickels > 0:
        print(f"{nickels} Nickels")
    if pennies > 0:
        print(f"{pennies} Pennies")
    else:
        print("No Change")


if __name__ == "__main__":
    main()
