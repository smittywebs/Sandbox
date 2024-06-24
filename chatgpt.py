import turtle

# Function to draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

# Function to draw a regular polygon (octagon)
def draw_octagon(size):
    for _ in range(8):
        turtle.forward(size)
        turtle.left(45)

# Set up the turtle
turtle.speed(0)  # Set the speed of drawing (1 is slowest, 10 is fastest)
turtle.bgcolor("lightblue")  # Set background color to light blue

# Draw the rectangle
turtle.penup()
turtle.goto(-100, -50)  # Position the turtle
turtle.pendown()
turtle.color("green")  # Set outline color to green
turtle.begin_fill()  # Begin filling the shape
draw_rectangle(5, 100)  # Draw rectangle with width 200 and height 100
turtle.end_fill()  # End filling the shape

# Draw the octagon
turtle.penup()
turtle.goto(-125, 50)  # Position the turtle
turtle.pendown()
turtle.color("orange")  # Set outline color to orange
turtle.begin_fill()  # Begin filling the shape
draw_octagon(50)  # Draw octagon with side length 100
turtle.end_fill()  # End filling the shape

# Hide the turtle and display the result
turtle.hideturtle()
turtle.done()

