# David Redmond
# 29 June 2025
# P2 HW2
# Purpose make a program to to calculate total pay.


def main():
    name = input("Enter employee's name: ")
    hours = int(input("Enter number of hours worked. Integers only: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    overtime_hours = 0
    overtime_pay = 0

    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

    # Calc the reg hours based on if there is overtime.
    if hours > 40:
        reg_pay = pay_rate * (hours - overtime_hours)
    else:
        reg_pay = pay_rate * hours

    if overtime_hours > 0:
        gross_pay = reg_pay + overtime_pay
    else:
        gross_pay = reg_pay

    print(
        "---------------------------------------------------------------------------------"
    )
    print(f"Employee Name: {name:>3}")
    print("\n")
    print(
        f"{'Hours Worked':<7}   {'Pay Rate':>7}   {'OverTime':>7}   {'OverTime Pay':>7}   {'RegHour Pay':>7}   {'Gross Pay':>7}"
    )
    print(
        "---------------------------------------------------------------------------------"
    )
    print(
        f"{hours:<7.2f} {'$':>8}{pay_rate:.2f} {overtime_hours:>10.2f} {'$':>7}{overtime_pay:.2f} {'$':>8}{reg_pay:.2f} {'$':>5}{gross_pay:.2f}"
    )


if __name__ == "__main__":
    main()
