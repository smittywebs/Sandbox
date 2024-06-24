import turtle
turtle.shape("turtle")
turtle.color("green")
turtle.speed(0)

def square(len):
   for i in range(4):
      turtle.width(5)
      turtle.forward(len)
      turtle.left(90)

square(100)

turtle.penup()
turtle.forward(150)
turtle.pendown()

length = 5
width = 100

for i in range(2):
   turtle.width(1)
   turtle.forward(length)
   turtle.right(90)
   turtle.forward(width)
   turtle.right(90)

def octagon(len):
    turtle.penup()
    turtle.backward(20)
    turtle.pendown()
    for i in range(8):
        turtle.forward(len)
        turtle.left(45)
octagon(40)

turtle.Screen().exitonclick()

