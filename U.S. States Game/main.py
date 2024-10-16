import turtle as t
import pandas # type: ignore

screen = t.Screen()
screen.title("US State Game")
image = r"D:\PYTHON\PYTHON - Udemy\Game\U.S. States Game\blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pandas.read_csv(r"D:\PYTHON\PYTHON - Udemy\Game\U.S. States Game\50_states.csv")
all_state = data["state"].to_list()
guessed_state = []

while len(guessed_state)<50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Correct",prompt="What's state's name").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        print(missing_state)
        break

    if answer_state in  all_state:
        guessed_state.append(answer_state)
        tut = t.Turtle()
        tut.hideturtle()
        tut.penup()
        stae_data = data[data.state==answer_state]
        tut.goto(int(stae_data.x),int(stae_data.y))
        tut.write(answer_state)
