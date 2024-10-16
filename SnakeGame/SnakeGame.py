import turtle
import snake
import time
import food
import scoreboard

screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[0].distance(food)<15:
        food.refresh()
        scoreboard.increScore()
        snake.extend()

    if snake.turtles[0].xcor()>280 or snake.turtles[0].xcor()<-280 or snake.turtles[0].ycor()>280 or snake.turtles[0].ycor()<-280:
        scoreboard.game_over()
        scoreboard.reset()
        game_is_on = False

    for tut in snake.turtles:
        if tut==snake.turtles[0]:
            pass
        elif snake.turtles[0].distance(tut)<10:
            game_is_on = False
            scoreboard.reset()
            scoreboard.game_over()
            

screen.exitonclick()