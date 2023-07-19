from turtle import Turtle
class Ball:
    def __init__(self, x=0, y=0):
        self.turtle = Turtle(shape="circle")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.initial_direction = [1, 1]
        self.direction = [1, 1]
        self.speed = 10
        self.initial_speed = 10
        self.increment_speed = 1

    def reset_position(self):
        self.turtle.goto(0, 0)
        self.speed = self.initial_speed
        self.change_x_direction()
        #self.direction = [-1 * self.initial_direction[0], -1 * self.initial_direction[1]]
        #self.initial_direction = self.direction.copy()

    def change_y_direction(self):
        self.direction[1] = self.direction[1] * -1

    def change_x_direction(self):
        self.direction[0] = self.direction[0] * -1

    def add_speed(self):
        self.speed += self.increment_speed

    def move_ball(self):
        self.turtle.setposition(
            self.turtle.xcor() + (self.speed * self.direction[0]),
            self.turtle.ycor() + (self.speed * self.direction[1])
        )
