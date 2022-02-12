from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):

        self.clear()
        self.goto(-200, 244)
        self.write(self.score, align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

