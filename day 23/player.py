from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
        self.new_y_cor = 10
        self.new_x_cor = 0



    def move_player(self):
        new_y = self.ycor() + self.new_y_cor
        new_x = self.xcor() + self.new_x_cor
        self.goto(new_x, new_y)

    def reset_pos(self):
        self.goto(0, -280)
