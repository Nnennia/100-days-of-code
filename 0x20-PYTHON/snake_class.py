from turtle import Turtle
X_INDEX = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for index in X_INDEX:
            snake_n = Turtle("square")
            snake_n.color("white")
            snake_n.penup()
            snake_n.goto(index)
            self.segment.append(snake_n)

    def move(self):
        flag = True
        while flag:
            for seg_num in range(len(self.segment) - 1, 0, -1):
                xco = self.segment[seg_num - 1].xcor()
                yco = self.segment[seg_num - 1].ycor()
                self.segment[seg_num].goto(xco, yco)
            return self.segment[0].forward(MOVE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
