import time
from turtle import  Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Dr. palazzo's snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score_b = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down" )
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left" )
screen.onkey(score_b.pause_game, "space")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    if  score_b.is_paused:
        snake.move()

    #to detect collision with food
        if snake.head.distance(food) < 15:
            food.change_position()
            score_b.update_score()
            snake.extend_snake()
            #to  increase the food size for more points
            if score_b.score % 5 == 0:
                food.make_food_bigger()
                score_b.make_food_bigger()


            else:
                food.small_food()

        #to detect collision to wall
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            score_b.high_score()
            snake.reset_pos()


        #to detect collision to tail
        for square in snake.all_squares[1:]:
            if snake.head.distance(square) < 10:
                score_b.high_score()





























screen.exitonclick()
