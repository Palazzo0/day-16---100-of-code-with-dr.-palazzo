import turtle
from turtle import Turtle, Screen
import random

color_palette = [(229, 225, 221), (231, 206, 85), (218, 229, 219),
                 (231, 222, 226), (224, 150, 89), (215, 224, 230), (120,
                 166, 185), (159, 14, 21), (34, 110, 157), (232, 82, 46), (124, 176, 144),
                 (8, 97, 38), (171, 21, 16), (199, 65, 28),
                 (185, 186, 27), (31, 128, 47), (12, 41, 74), (15, 63, 40), (242, 202, 5),
                 (138, 82, 95), (85, 15, 22), (51, 166, 77), (44, 26, 22), (6, 65, 137), (173, 135, 149),
                 (232, 170, 160), (48, 150, 195), (219, 66, 71), (74, 135, 186), (169, 206, 175), (225, 172, 175),
                 (162, 203, 212), (173, 190, 214), (43, 71, 75), (64, 69, 52), (246, 12, 11), (248, 10, 19)]
print(color_palette[20:])
# print(len(color_palette))
# jack = Turtle()
# jack.speed("fastest")
# turtle.colormode(255)
# #TODO 1: set the fxn to draw dotted lines
# def draw_dots(start_x, start_y, length, dot_spacing):
#     jack.penup()
#     jack.hideturtle()
#     jack.goto(start_x, start_y)
#     for _ in range(length // (2 * dot_spacing)):
#         jack.dot(20, random.choice(color_palette))
#         jack.penup()
#         jack.forward(dot_spacing)
#
# # TODO 2: to draw parallel lines on top of each other:
# start_x = -200
# start_y = -150
# line_length = 1000
# line_space = 50
# dot_spacing = 50
#
# #TODO 3: to set the number of lines:
# for line in range(10):
#     draw_dots(start_x, start_y + line *  line_space, line_length, dot_spacing)
#
#
#
#
#
# screen = Screen()
# screen.exitonclick()