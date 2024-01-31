from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.color("black")
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_end(self):
        self.reset()
        self.goto(0, 0)
        self.write(f"GAME OVER\n Score: {self.score}", align="center", font=FONT)


