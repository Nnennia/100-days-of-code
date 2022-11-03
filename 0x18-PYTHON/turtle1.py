from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("red")
for _ in range(4):
    tim.forward(100)
    tim.left(90)

for i in range(10):
    tim.forward(15)
    tim.penup()
    tim.forward(15)
    tim.pendown()
screen.exitonclick()
