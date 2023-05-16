from turtle import Turtle
FONT=("Courier", 21, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=-30, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= "center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align= "center", font=FONT)
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()




