# David Redmond
# 22 June 2025
# P2 HW2
# Purpose is accept grades and display the lowest, highest, sum, and average while including a loop and
# modified list dropping the lowest grade.


def main():
    print("----This program calculates overall grades-----\n")

    user_num = int(input("How many scores do you want to enter? "))
    list_of_grades = []
    it = 1

    while it <= user_num:
        grade = int(input(f"Enter Score #{it}: "))
        if grade < 0 or grade > 100:
            print("INVALID Score Entered!!!")
            print("Score should be between 0 and 100")
        else:
            list_of_grades.append(grade)
            it += 1

    lowest_grade = min(list_of_grades)

    list_of_grades.remove(lowest_grade)

    sum_of_grades = sum(list_of_grades)

    # Expression is x / 6 with x being the sum of grades.
    average_of_grades = sum(list_of_grades) / len(list_of_grades)

    if average_of_grades > 89:
        letter_grade = "A"
    elif average_of_grades > 79:
        letter_grade = "B"
    elif average_of_grades > 69:
        letter_grade = "C"
    else:
        letter_grade = "F"

    print("\n")
    print("--------------------Results--------------------\n")

    print(f"Lowest Grade: {lowest_grade:>7.1f}")
    # print(f"Highest Grade: {highest_grade:>6.1f}")
    print(f"Modified List: {list_of_grades}")
    print(f"Sum of Grades: {sum_of_grades:>7.1f}")
    print(f"Average: {average_of_grades:>13.2f}")
    print(f"Grade: {letter_grade:>13}")

    print("-----------------------------------------------\n")


if __name__ == "__main__":
    main()
