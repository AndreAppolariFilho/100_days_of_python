from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_body = []
        self.current_direction = "right"
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((0 - i * 20, 0))
    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.goto(position)
        turtle.color("white")
        self.snake_body.append(turtle)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def update_body_position(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)

    def move_forward(self):
        self.update_body_position()
        self.head.forward(20)

    def rotate_right(self):
        if self.current_direction != "left":
            self.head.setheading(0)
            self.current_direction = "right"

    def rotate_up(self):
        if self.current_direction != "down":
            self.head.setheading(90)
            self.current_direction = "up"

    def rotate_down(self):
        if self.current_direction != "up":
            self.head.setheading(270)
            self.current_direction = "down"

    def reset(self):
        for seg in self.snake_body:
            seg.reset()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def rotate_left(self):
        if self.current_direction != "right":
            self.head.setheading(180)
            self.current_direction = "left"
