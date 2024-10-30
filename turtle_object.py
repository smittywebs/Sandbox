import turtle

def draw_arc(turtle, size, curves, x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(90)
    for points in range(curves):
        turtle.forward(size/curves)
        turtle.right(90/curves)

def create_turtle(turtle, paint, w):
    turtle.shape("turtle")
    turtle.color(paint)
    turtle.speed(15)
    turtle.width(w)

def draw_rainbow():
    i = 0
    colorsList = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for c in colorsList:
        colorsList[i] = turtle.Turtle()
        create_turtle(colorsList[i], c, 25)
        draw_arc(colorsList[i], 450, 20, (-175 + 25 * i), -175)
        i += 1

draw_rainbow()