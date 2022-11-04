import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()
    if player.finish_line():
        player.go_to()
        car.level_up()
        score.increase()
screen.exitonclick()
