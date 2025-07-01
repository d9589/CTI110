# David Redmond
# 22 June 2025
# P2 LAB1
# Purpose is to calculate the measurements of a circle and to our the desired info.


def main():
    # Casting radius to a float from input.
    radius = float(input("What is the radius of the circle?: "))

    # Calculations.
    diameter = 2 * radius
    circumference = 2 * 3.14 * radius
    area = 3.14 * radius**2

    print(f"The diameter of the circle is {diameter:.1f}")
    print(f"The circumference of the circle is {circumference:.2f}")
    print(f"The area of the circle is {area:.3f}")


if __name__ == "__main__":
    main()
