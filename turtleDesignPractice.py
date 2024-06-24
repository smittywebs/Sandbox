import turtle

turtle.shape("turtle")
turtle.speed(0)
turtle.color("green")
turtle.bgcolor("black")

def spiral(len):
    for i in range(6):
     for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        turtle.color(colours)
        turtle.circle(len)
        turtle.left(50)
        turtle.hideturtle()

def main():
   turtle.pensize(2)
   turtle.penup()
   turtle.sety(100)
   turtle.pendown()
   spiral(50)
   turtle.penup()
   turtle.sety(-100)
   turtle.pendown()
   spiral(50)
   turtle.penup()
   turtle.home()
   turtle.penup()
   turtle.setx(-130)
   turtle.pendown()
   spiral(50)
   turtle.penup()
   turtle.home()
   turtle.penup()
   turtle.setx(130)
   turtle.pendown()
   spiral(50)
   
   
    
main()
turtle.Screen().exitonclick()