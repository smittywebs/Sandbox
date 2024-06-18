import turtle

turtle.shape("turtle")
turtle.color("green")
turtle.speed(0)

for i in range(8):
    turtle.forward(50)
    turtle.left(45)

turtle.forward(20)
turtle.forward(10)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(100)
turtle.hideturtle()
        



turtle.Screen().exitonclick()