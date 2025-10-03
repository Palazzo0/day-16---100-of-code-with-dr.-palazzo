import turtle
from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 15, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../data.txt") as data:
            content = int(data.read())

        self.highest_score = content
        self.color("white")
        self.penup()
        self.goto(x=-10, y= 270 )
        self.hideturtle()
        self.is_paused = False
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} Highest Score:{self.highest_score} ", align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME 0VER ", align=ALIGN, font=FONT)

    def high_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("../../data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")

        self.score = 0
        self.update_scoreboard()

    def update_score(self):
        self.score += 1

        self.update_scoreboard()

    def pause_game(self):
        self.is_paused = not self.is_paused

    def make_food_bigger(self):
        self.score += 5


