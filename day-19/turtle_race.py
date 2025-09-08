from turtle import Turtle, Screen
screen = Screen()
import random
screen.setup(width=500, height=400)
user_bet = screen.textinput("Welcome to the turtle race.", "Choose the colour of turtle that would win:")
race_on = False
all_turtles =[]


turtle_color = ["red", "green", "yellow", "blue", "purple", "orange"]

y_pos = [-100, -70, -40, -10, 20, 50]


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)
print(all_turtles)
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            race_on = False
            if winning_color == user_bet :
                print(f"You have won the bet. The color of the winning turtle is {winning_color} ")
            else:
                print(f"You have lost the bet. The color of the winning turtle is {winning_color} ")
        random_pace = random.randint(0, 10)
        turtle.forward(random_pace)




screen.exitonclick()