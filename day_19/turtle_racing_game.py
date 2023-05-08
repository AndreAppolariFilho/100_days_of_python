import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(
    width=500,
    height=400
)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtles = []

for i, color in enumerate(colors):
    turtle = Turtle(shape='turtle')
    turtle.penup()
    turtle.goto(
        x=-1 * screen.window_width()/2 + 10,
        y=-1*screen.window_height()/4 + i * 40)
    turtle.color(color)
    turtles.append(turtle)

is_race_on = False

winning_turtle = ''

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= screen.window_width()/2 - 20:
            is_race_on=False
            winning_turtle = turtle.pencolor()
            break
if winning_turtle == user_bet:
    print(f"You've won {winning_turtle} turtle is the winner!")
else:
    print(f"You've lost {winning_turtle} turtle is the winner!")
screen.exitonclick()
