# David Redmond
# 7 July 2025
# P4 LAB1
# Purpose is display a multiplication table with x * 1 ~ 12.


def main():
    while True:
        user_int = int(input("Enter an integer: "))

        if user_int >= 0:
            for num in range(1, 13):
                total = user_int * num
                print(f"{user_int} * {num} = {(total)}")
        else:
            print("This program does not handle negative numbers nor floats.")

        while True:
            user_choice = str(input("Would you like to run the program again? "))

            if user_choice == "yes":
                break
            elif user_choice == "no":
                print("Exiting program...")
                exit(0)
            else:
                print("We only accept yes or no here buddy.")
                continue


if __name__ == "__main__":
    main()
