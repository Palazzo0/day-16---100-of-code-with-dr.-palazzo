from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 48, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_s()
    def update_s(self):
        self.clear()
        self.goto(-100, 240)
        self.write(f"{self.l_score}", align=ALIGN, font=FONT)
        self.goto(100, 240)
        self.write(f"{self.r_score}", align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_s()

    def r_point(self):
        self.r_score += 1
        self.update_s()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME 0VER ", align=ALIGN, font=FONT)