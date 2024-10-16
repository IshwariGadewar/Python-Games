import turtle as t


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 20
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        
    def ball_passed(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.x_bounce()