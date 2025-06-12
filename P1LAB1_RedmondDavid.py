# David Redmond
# 12 June 2025
# P1 LAB1
# Purpose is to accept string values, the names, and output a statement in the console when run.


def main():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    print("Hello,", f_name, l_name + "!", "Welcome to CTI-110")
    # Specifically used l_name + "!" to make ! sit against the last name.
    # Otherwise there is a space, which is expected bahavior.


if __name__ == "__main__":
    main()

# I use Python weekly, so structuring this as normal is a habit.
# While __name__ is not exactly required at the moment, I like order.
