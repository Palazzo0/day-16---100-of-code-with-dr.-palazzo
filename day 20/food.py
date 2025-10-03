from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.penup()
        self.change_position()

    def change_position(self):
        random_x = random.randint(-280, 280)
        random_y =  random.randint(-280, 280)
        self.goto(random_x, random_y)

    def small_food(self):
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)


    def make_food_bigger(self):

        self.shapesize(stretch_wid=1, stretch_len=1)
        # self.change_position()
