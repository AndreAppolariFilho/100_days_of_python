from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.load_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def load_highscore(self):
        with open("data.txt") as file:
            self.high_score = int(file.readline().strip())

    def write_highscore(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def reset(self):
        self.high_score = max(self.score, self.high_score)
        self.score = 0
        self.update_scoreboard()
        self.write_highscore()

    #def game_over(self):
    #    self.color("red")
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
