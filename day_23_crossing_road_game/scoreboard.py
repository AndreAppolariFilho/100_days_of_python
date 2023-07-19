from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard:
    def __init__(self):
        self.score = 1
        self.turtle = Turtle()
        self.turtle.color("black")
        self.turtle.penup()
        self.turtle.goto(-280, 250)
        self.draw_score_board()
        self.turtle.hideturtle()

    def draw_score_board(self):
        self.turtle.clear()
        self.turtle.write(f"Level: {self.score}", font=FONT)

    def update_level(self):
        self.score += 1
        self.draw_score_board()

    def draw_game_over(self):
        self.turtle.goto(0, 0)
        self.turtle.color("red")
        self.turtle.write("Game Over", align="Center", font=FONT)
