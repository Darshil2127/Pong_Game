from turtle import Turtle, Screen

screen = Screen()

screen.bgcolor("Black")
screen.setup(width=800 , height=600)
screen.title("Pong")
screen.tracer(0) # turn of the animation
# when you turn it off, you need to call screen.update function manually
player_1 = Turtle()
player_1.shape("square")
player_1.color("white")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(x=380, y=0)

def go_up():
    new_y = player_1.ycor() + 20 #add 20 into y position
    player_1.goto(player_1.xcor(), new_y)

def go_down():
    new_y = player_1.ycor() -  20 #add 20 into y position
    player_1.goto(player_1.xcor(), new_y)

screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()