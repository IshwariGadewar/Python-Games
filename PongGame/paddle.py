import turtle as t


class Paddle(t.Turtle):
    def __init__(self,posi):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(posi)

    def down(self):
        self.goto(self.xcor(),self.ycor()-50)

    def up(self):
        self.goto(self.xcor(),self.ycor()+50)
