from paddle import Paddle
from turtle import Screen
from ball import Ball
import time
from score_board import ScoreBoard

screen=Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title("pong")
screen.tracer(0)

right_paddle=Paddle((350,0))
left_paddle =Paddle((-350,0))
ball=Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=right_paddle.up,key="Up")
screen.onkey(fun=right_paddle.down,key="Down")
screen.onkey(fun=left_paddle.up,key="w")
screen.onkey(fun=left_paddle.down,key="s")

game_on =True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()


    if ball.distance(right_paddle)<50 and ball.xcor()>320 or  ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()
