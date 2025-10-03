import random

import turtle
from turtle import  Turtle, Screen
import random
tim = Turtle()
turtle.colormode(255)
def color_mode():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
tim.speed("fastest")
#TODO 2: TO DRAW A SPIROGRAPH
def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        tim.color(color_mode())
        tim.circle(50)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)


#TODO 1: DRAW DIFFERENT SHAPES FROM SQUARE TO TRIANGLE , PENTAGON ETC

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         tim.forward(50)
#         tim.right(angle)
#
# for num_of_sides in range(3, 11):
#     draw_shape(num_of_sides)

#TODO: DRAW DASHED LINES

# for _ in range(10):
#     #
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()




