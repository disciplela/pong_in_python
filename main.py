from turtle import Screen, Turtle
from pong import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
background = Turtle()
screen.addshape('tron-background.gif')
background.shape('tron-background.gif')
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(l_paddle.up, 'e')
screen.onkeypress(l_paddle.down, 'd')
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down   ')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    screen.listen()
    ball.move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
    #Detect collision wtih paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when r_paddle misses

    if ball.xcor() < -380:
        ball.reset_direction()
        scoreboard.r_point()
        scoreboard.update_score()

    if ball.xcor() > 380:
        ball.reset_direction()
        scoreboard.l_point()
        scoreboard.update_score()

screen.exitonclick()


