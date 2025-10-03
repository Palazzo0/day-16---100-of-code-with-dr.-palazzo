from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.increase_speed = 0.1
        self.new_x_cor = 5
        self.new_y_cor = 5


    def move_ball(self):
        new_y = self.ycor() + self.new_y_cor
        new_x =  self.xcor() + self.new_x_cor
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.new_y_cor *= -1
        self.increase_speed *= 0.9


    def bounce_x(self):
        self.new_x_cor *= -1

    def refresh_pos(self):
        self.goto(0, 0)
        self.increase_speed = 0.1
        self.bounce_x()

