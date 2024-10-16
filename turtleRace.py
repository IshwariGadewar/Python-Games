import turtle as t
import random

screen = t.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race?Enter a color: ")

colors = ["red","orange","yellow","green","blue","purple"]
j = -100
all_turtle =[]

for _ in range(6):
    tim = t.Turtle(shape="turtle")
    tim.color(colors[_])
    tim.penup()
    tim.goto(x=-230,y=j + (_*40))
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in  all_turtle:
        if turtle.xcor()>230:
            winning = turtle.pencolor()
            if winning==user_bet:
                print(f"You've won! The {winning} turtle is the winner")
            else:
                print(f"The {winning} turtle is the winner. You Lost")
            is_race_on = False
        dist = random.randint(0,10)
        turtle.forward(dist)

screen.exitonclick()