import time
from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Dr. palazzo's pong game.")
screen.tracer(0)


r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score_b = Scoreboard()







screen.listen()

screen.onkey(r_paddle.move_paddle_up, "Up")
screen.onkey(r_paddle.move_paddle_down, "Down")

screen.onkey(l_paddle.move_paddle_up, "w")
screen.onkey(l_paddle.move_paddle_down, "s")


game_on =True

while game_on:
    time.sleep(ball.increase_speed)
    screen.update()
    ball.move_ball()

    #detect ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #the ball should bounce
        ball.bounce_y()
    #detect collision with the two paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() >340 or ball.distance(l_paddle) <50 and ball.xcor() < -340:
        ball.bounce_x()
    #detect when the right paddle misses the ball
    if ball.xcor() >380 :
        ball.refresh_pos()
        score_b.l_point()
#to detect when game is over
    if score_b.l_score == 10 or score_b.r_score == 10:
        game_on = False
        score_b.game_over()



    #detect when the left paddle misses the ball
    if ball.xcor() <-380 :
        ball.refresh_pos()
        score_b.r_point()


screen.exitonclick()