from turtle import Turtle

class ScoreBoard(Turtle):
    def __int__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
