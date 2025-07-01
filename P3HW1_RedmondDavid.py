# David Redmond
# 29 June 2025
# P3 HW1
# Purpose is to fix the bugs.


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 1: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum_grades = sum(grades)
avg = sum(grades) / len(grades)

# determine letter grade for average

print("\n")
print("--------------------Results--------------------\n")

print(f"Lowest Grade: {low:>7.1f}")
print(f"Highest Grade: {high:>6.1f}")
print(f"Sum of Grades: {sum_grades:>7.1f}")
print(f"Average: {avg:>13.2f}")

print("-----------------------------------------------\n")

if avg >= 90:
    print("Your grade is: A")
elif avg > 80:
    print("Your grade is: B")
else:
    print("Your grade is: F")  # TO DO: finish this
