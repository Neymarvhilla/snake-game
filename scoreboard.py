from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
        print(self.score)


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over\nFinal Score: {self.score}", align=ALIGNMENT, font=FONT)



