import time
from turtle import Screen
from player import Player
from cars import Cars
from level import Level

screen = Screen()

screen.setup(width=600, height=600)
screen.title("Dr. palazzo's turtle crossing game.")
screen.tracer(0)


player = Player()
cars = Cars()
level = Level()
screen.listen()
screen.onkey(player.move_player, "Up")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(cars.increase_speed)
    cars.car_movement()
    #detect when player has reached the other side
    if player.ycor() == 290:
        player.reset_pos()
        level.new_level()
        cars.increase_s()
    #detect collision with car
    for car in cars.all_cars:
        if player.distance(car) <25:
            game_is_on = False
            level.game_over()





screen.exitonclick()