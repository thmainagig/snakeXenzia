from turtle import Turtle
FONT=("Courier", 21, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(x=-30, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}", align= "center", font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over. High Score: {self.high_score}", align= "center", font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as f:
                f.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()




