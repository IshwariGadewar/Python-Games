import turtle

MOVE_DISTANCE = 20
positions = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for pos in positions:
            new_seg = turtle.Turtle(shape="square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(pos)
            self.turtles.append(new_seg)

    def move(self):
        for tut in range(len(self.turtles)-1,0,-1):
            newx = self.turtles[tut-1].xcor()
            newy = self.turtles[tut-1].ycor()
            self.turtles[tut].goto(newx,newy)
        self.turtles[0].forward(MOVE_DISTANCE) 

    def add_turtle(self,position):
        new_seg = turtle.Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.turtles.append(new_seg)

    def extend(self):
        self.add_turtle(self.turtles[-1].position())
        

    def up(self):
        if self.turtles[0].heading()!=270:
            self.turtles[0].setheading(90)  

    def down(self):
        if self.turtles[0].heading()!=90:
            self.turtles[0].setheading(270)    

    def left(self):
        if self.turtles[0].heading()!=0:
            self.turtles[0].setheading(180) 

    def right(self):
        if self.turtles[0].heading()!=180:
            self.turtles[0].setheading(0)      