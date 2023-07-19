from turtle import Turtle

class Paddle:
    def __init__(self, x=350, y=0):
        self.turtle = Turtle(shape="square")
        self.turtle.color("white")
        self.turtle.shapesize(stretch_wid=100/20, stretch_len=1)
        self.turtle.penup()
        self.turtle.goto(x, y)

    def go_up(self):
        self.turtle.sety(self.turtle.ycor() + 20)

    def go_down(self):
        self.turtle.sety(self.turtle.ycor() - 20)
