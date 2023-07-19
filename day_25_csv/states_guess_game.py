import turtle
import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

dataframe = pandas.read_csv("50_states.csv")

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's ?")
    if answer_state == "Exit":
        break
    for i in dataframe.index:
        if answer_state.lower() == dataframe["state"][i].lower():
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(dataframe["x"][i], dataframe["y"][i])
            t.write(dataframe["state"][i])
            t.color("black")
            guessed_states.append(dataframe["state"][i])
            break

states_to_learn = [
    dataframe["state"][i]
    for i in dataframe.index
    if not dataframe["state"][i] in guessed_states
]

pd.DataFrame({
    "States":states_to_learn
}).to_csv("states_to_learn.csv")
