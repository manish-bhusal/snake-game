from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.inc_score()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score:{self.score} High Score: {self.highscore} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                # data.write(f"{self.highscore}")
                data.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.color("red")

    def inc_score(self):
        self.update_scoreboard()
        self.score += 1
