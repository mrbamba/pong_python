from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#158abd")
screen.title("Welcome to Pong!")
screen.tracer(0)

# Draw middle line:
line = Turtle()
line.penup()
line.width(5)
line.color("white")
line.goto(0, -300)
line.pendown()
line.hideturtle()
for y in range(-300, 320, 20):
    line.pendown()
    line.goto(0, y-15)
    line.penup()
    line.goto(0, y)

# Set up the game variables
game_is_on = True
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = Scoreboard()


# Listen to events
screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

# Main game loop
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move_ball()
    # scoreboard.update_scoreboard()

    # Detect collision with right paddle
    if ball.xcor() == 340:
        if ball.distance(r_paddle) < 65:
            ball.change_direction()
            ball.speed_up()

    # Detect collision with left paddle
    elif ball.xcor() == -340:
        if ball.distance(l_paddle) < 65:
            ball.change_direction()
            ball.speed_up()

    # Detect collision with side of paddle
    elif ball.xcor() > 340 and ball.distance(r_paddle) < 70 or ball.xcor() < -340 and ball.distance(l_paddle) < 70:
        ball.bounce()

    # Detect ball out of bounds
    if ball.xcor() < -400:
        scoreboard.right_point()
        ball.reset_position()
    elif ball.xcor() > 400:
        scoreboard.left_point()
        ball.reset_position()

    # Detect collision with upper/lower wall
    if ball.ycor() > 275 or ball.ycor() < -270:
        ball.bounce()

screen.exitonclick()
