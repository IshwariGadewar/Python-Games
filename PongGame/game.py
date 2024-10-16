import turtle
import paddle
import ball
import time
import scoreboard

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = paddle.Paddle((380,0))
l_paddle = paddle.Paddle((-380,0))
score = scoreboard.ScoreBoard()
mBall = ball.Ball()

screen.listen()
screen.onkey(r_paddle.up,key="Up")
screen.onkey(r_paddle.down,key="Down")
screen.onkey(l_paddle.up,key="w")
screen.onkey(l_paddle.down,key="s")

game_is_on = True

while game_is_on:
    time.sleep(mBall.move_speed)
    screen.update()
    mBall.move()

    if mBall.xcor()>380:
        mBall.ball_passed()
        score.increLrfy()

    if mBall.xcor()<-380:
        mBall.ball_passed()
        score.increRight()

    if mBall.ycor()>290 or mBall.ycor()<-290:
        #bounce
        mBall.y_bounce()
    
    if mBall.distance(r_paddle)<50 and mBall.xcor()>350:
        mBall.x_bounce()              

    if mBall.distance(l_paddle)<50 and mBall.xcor()<-350:
        mBall.x_bounce()  

    if score.rscore>5 or score.lscore>5:
        game_is_on = False
        if(score.rscore>5):
            score.RightWin()     
        if(score.lscore>5):
            score.LeftWin()     

screen.exitonclick()