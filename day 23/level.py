from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 15, "normal")
class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-230, 270)
        self.new_level()
    # def write_level(self):


    def new_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level} ", align=ALIGN, font=FONT )

        # self.write_level()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME 0VER! ", align=ALIGN, font=FONT)