import random
import turtle
from turtle import Turtle

car_color = ["brown", "BlueViolet", "DarkSlateGray", "cyan", "DarkOrchid4",
             "DarkBlue", "DarkGreen","CornflowerBlue", "DarkSlateBlue", "black",
             "coral4","chocolate", "chartreuse4", "blue4","chocolate4","DarkOrange", "DeepPink4","DarkRed",
             "DarkKhaki","brown4", "DarkMagenta","DarkSeaGreen","cyan4","DarkOliveGreen4","DarkSalmon",
             "DeepSkyBlue","DarkViolet", "blue3","chartreuse3","DarkOliveGreen3"]

all_cars =[]
# POSITIONS = [(290, -160), (260, -100), (200, -60), (240, -20), (200, 40),(180,80),(290,120), (110,160),(250, 200),(270,240)]

x_pos = [-290, -290, 260, 270, -280, -260, 180, -290, -110, -250, 270, -210, -280, -200, -230,
         -200, -290, 260, 270, -260, -200, 180, -290, -110, -250, 270, -210, -280, 230, -230]

y_pos = [-160,-100, -60, -20, 40, 80, 120, -130, -200, 100, 160,
         200, 240, -160, 70, -140,-100, -80, -50, 150, 80, 100, -130, -180, 120, 140, 200, 260, -140, 100]


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.increase_speed = 0.1
        self.pace = 10
        self.create_cars()



    def create_cars(self):
        for car_index in range(29):
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(car_color[car_index])
            new_car.penup()
            new_car.goto(x=x_pos[car_index], y=y_pos[car_index])
            self.all_cars.append(new_car)
            self.car_movement()


    def car_movement(self):

            for car in self.all_cars:
                car.forward(self.pace)
                self.reset_car()

    def increase_s(self):
        self.reset_car()
        self.increase_speed *=5

    def reset_car(self):
        for c in self.all_cars:
            if c.xcor() < -300:
                self.increase_speed = 0.1
                c.goto(x= 290, y=y_pos[self.all_cars.index(c)])

