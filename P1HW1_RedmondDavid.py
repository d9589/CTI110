# David Redmond
# 12 June 2025
# P1 HW1
# Purpose is to accept integers, perform arithmetic and output a statement in the console when run.


def main():
    # We are not allowed to use try/except or any validation, so strings will any of the vars.
    print("-----" + "Calculating Exponents" + "-----\n")
    base_value = int(input("Enter an integer as the base value: "))
    exponent = int(input("Enter an integer as the exponent: "))
    print("\n")
    result_1 = base_value**exponent

    # I would personally use an f-string here. It's neater.
    print(base_value, "raised to the power of", exponent, "is", result_1, "!!")
    print("\n")

    # I could reuse the earlier variables since this is pretty inline and static
    # but not sure if allowed too based on the or if that is jumping to far ahead of the module.
    print("-----" + "Addition and Subtraction" + "-----\n")
    start_num = int(input("Enter a starting integer: "))
    add_num = int(input("Enter an integer to add: "))
    subtract_num = int(input("Enter an integer to subtract: "))
    result_2 = start_num + add_num - subtract_num
    print("\n")
    print(start_num, "+", add_num, "-", subtract_num, "is equal to", result_2)


if __name__ == "__main__":
    main()
