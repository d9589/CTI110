# David Redmond
# 7 July 2025
# P4 LAB1
# Purpose is to draw a square and a triangle using the turtle module.
# Angled the triangle just to be different.

import turtle


def main():
    turtle.title("CTI-110")  # Since it's tkinter, I can name it like this.
    # Add some color, size, and conditions.
    turtle.colormode(255)  # Have to set globally.
    square = turtle.Turtle()
    square.width(5)
    square.color(42, 185, 181)
    square.shape("turtle")  # Make the cursor a turtle.
    sqr_sides = 4

    triangle = turtle.Turtle()
    triangle.width(3)
    triangle.color(42, 185, 181)
    triangle.shape("turtle")  # Make the cursor a turtle.
    tri_sides = 3

    while sqr_sides > 0:
        # Draw a square.
        square.forward(100)
        square.left(90)
        sqr_sides -= 1
    else:
        # Draw a triangle
        square.hideturtle()
        triangle.forward(100)
        triangle.left(90)
        triangle.forward(50)
        triangle.left(60)
        triangle.forward(70)
        triangle.left(120)
        triangle.forward(70)
        triangle.left(120)
        triangle.forward(70)

        # Hide the turtle at the end to make it look clean.
        triangle.hideturtle()

    # TLDR: turtle is based on tkinter, so we throw a mainloop here so it doesn't error out.
    # It should work smoother.
    turtle.mainloop()


if __name__ == "__main__":
    main()
