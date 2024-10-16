import turtle as t

PATH = 'D:/PYTHON/PYTHON - Udemy/Game/SnakeGame/scores.txt'

class ScoreBoard(t.Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = 0
        f = open(PATH,mode='r')
        self.highScore = f.read()
        f.close()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highScore}",False,align="center",font=("Arial",20,"normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER\nScore = {self.score}",align="center",font=("Arial",24,"normal"))

    def increScore(self):
        self.score+=1   
        self.update_score()
        
    def reset(self):
        if str(self.score) > self.highScore:
            f = open(PATH,mode='w')
            f.write(f'{self.score}')
            f.close()