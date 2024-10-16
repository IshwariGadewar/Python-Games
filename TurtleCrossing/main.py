import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.bgcolor("white")

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_forward,key="Up")
screen.onkey(player.move_backward,key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.cars_move()

    for car in  cars.all_cars:
        if car.distance(player)<20:
            score.game_over()
            game_is_on = False

    if player.ycor() > 280:
        score.increScore()
        player.restart()
        cars.speed_up()


screen.exitonclick()