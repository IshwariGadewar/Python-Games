import turtle as t

FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(self.score,align="center",font=FONT)

    def increScore(self):
        self.clear()
        self.score +=1
        self.write(self.score,align="center",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)

