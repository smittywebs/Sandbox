import turtle

def rectangle(len):
    for i in range(4):
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(5)
        

def octagon(len):
    for i in range(8):
        turtle.forward(40)
        turtle.left(45)

def sign(len):
    rectangle(len)
    turtle.penup()
    turtle.backward(20)
    turtle.pendown()
    octagon(len)

def main():
    turtle.speed(0)
    turtle.shape("turtle")
    turtle.color("blue")
    sign(100)
    turtle.penup()
    turtle.color("red")
    turtle.forward(150)
    turtle.pendown()
    sign(50)
    turtle.hideturtle()
main()
 
turtle.Screen().exitonclick()