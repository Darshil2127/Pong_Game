from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard
screen = Screen()

screen.bgcolor("Black")
screen.setup(width=800 , height=600)
screen.title("Pong")
screen.tracer(0) # turn of the animation
# when you turn it off, you need to call screen.update function manually

r_paddle = Paddle((350,0)) #(()) because use as a tuple
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and \
            ball.xcor() < -320:
        ball.bounce_x()

    #if r_paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #if l_paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()