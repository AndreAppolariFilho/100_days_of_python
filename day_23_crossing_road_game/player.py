from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player:

    def __init__(self):
        self.turtle = Turtle("turtle")
        self.turtle.color("black")
        self.turtle.penup()
        self.turtle.goto(STARTING_POSITION)
        self.turtle.setheading(90)

    def move_up(self):
        self.turtle.forward(MOVE_DISTANCE)

    def check_objective(self):
        return self.turtle.ycor() >= FINISH_LINE_Y

    def reset_position(self):
        self.turtle.goto(STARTING_POSITION)

