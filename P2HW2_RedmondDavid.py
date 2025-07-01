# David Redmond
# 22 June 2025
# P2 HW2
# Purpose is accept grades and display the lowest, highest, sum, and average.


def main():
    print("----This program calculates overall grades-----\n")

    mod1_grade = float(input("Enter Grade For Module 1: "))
    mod2_grade = float(input("Enter Grade For Module 2: "))
    mod3_grade = float(input("Enter Grade For Module 3: "))
    mod4_grade = float(input("Enter Grade For Module 4: "))
    mod5_grade = float(input("Enter Grade For Module 5: "))
    mod6_grade = float(input("Enter Grade For Module 6: "))

    # Can also do list_of_grades = [mod1_grade, mod2_grade, mod3_grade, etc]
    # Long lines are less neat though.
    list_of_grades = []
    list_of_grades.append(mod1_grade)
    list_of_grades.append(mod2_grade)
    list_of_grades.append(mod3_grade)
    list_of_grades.append(mod4_grade)
    list_of_grades.append(mod5_grade)
    list_of_grades.append(mod6_grade)

    lowest_grade = min(list_of_grades)
    highest_grade = max(list_of_grades)
    sum_of_grades = sum(list_of_grades)

    # Expression is x / 6 with x being the sum of grades.
    average_of_grades = sum(list_of_grades) / len(list_of_grades)

    print("\n")
    print("--------------------Results--------------------\n")

    print(f"Lowest Grade: {lowest_grade:>7.1f}")
    print(f"Highest Grade: {highest_grade:>6.1f}")
    print(f"Sum of Grades: {sum_of_grades:>7.1f}")
    print(f"Average: {average_of_grades:>13.2f}")

    print("-----------------------------------------------\n")


if __name__ == "__main__":
    main()
