import turtle as t

class ScoreBoard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.rscore  = 0
        self.lscore  = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.PrintScore()

    def PrintScore(self):
        self.goto(100,230)
        self.write(self.rscore,align="center",font=("Arial",50,"normal"))
        self.goto(-100,230)
        self.write(self.lscore,align="center",font=("Arial",50,"normal"))

    def increRight(self):
        self.rscore += 1
        self.clear()
        self.PrintScore()

    def increLrfy(self):
        self.lscore += 1
        self.clear()
        self.PrintScore()

    def RightWin(self):
        self.clear()
        self.goto(0,0)
        self.write("Right Won",align="center",font=("Arial",24,"normal"))

    def LeftWin(self):
        self.clear()
        self.goto(0,0)
        self.write("Left Won",align="center",font=("Arial",24,"normal"))