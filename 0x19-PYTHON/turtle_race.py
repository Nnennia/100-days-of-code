from turtle import Turtle, Screen
import random

flag = False
screen = Screen()

screen.setup(width=500, height=400)
user = screen.textinput(title="Make your bet", prompt="Which turtle"
                        "will win the race? Enter a clour: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_index = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_index[index])
    all_turtles.append(new_turtle)

if user:
    flag = True

while flag:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            flag = False
            win_color = turtle.pencolor()
            if win_color == user:
                print(f"You've won! The {win_color} is the winner")
            else:
                print(f"You've lost! The {win_color} is the winner")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
