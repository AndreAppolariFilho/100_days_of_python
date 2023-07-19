from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard:
    def __init__(self):
        self.turtle = Turtle()
        self.points_left = 0
        self.points_right = 0
        self.turtle.color("white")
        self.turtle.penup()
        self.draw_score_board()
        self.turtle.hideturtle()

    def update_scoreboard_left(self):
        self.points_left += 1
        self.draw_score_board()

    def update_scoreboard_right(self):
        self.points_right += 1
        self.draw_score_board()

    def draw_score_board(self):
        self.turtle.clear()
        self.turtle.goto(-100, 200)
        self.turtle.write(f"{self.points_left}", align=ALIGNMENT, font=FONT)
        self.turtle.goto(100, 200)
        self.turtle.write(f"{self.points_right}", align=ALIGNMENT, font=FONT)
