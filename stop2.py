import turtle
turtle.speed(0)
turtle.shape("turtle")

def octagon(width, color):
    for i in range(8):
        turtle.color(color)
        turtle.forward(width)
        turtle.left(45)

def rectangle(width, height, color):
    for i in range(2):
       turtle.color(color)
       turtle.forward(width)
       turtle.right(90)
       turtle.forward(height)
       turtle.right(90)

def stop(width, color):
    octagon(width, color)
    turtle.penup()
    turtle.forward(width * .375)
    turtle.pendown()
    rectangle(width * .2, width * 2, color)
    turtle.penup()

stop(width= 50, color= "red")
turtle.penup()
turtle.forward(150)
turtle.pendown()
stop(width = 20, color =  "blue")
turtle.hideturtle()
 
turtle.Screen().exitonclick()