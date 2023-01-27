from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        """Initializes the Ball object, super inherits the turtle module"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#ccff00")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.05
        self.move_ball()

    def move_ball(self):
        """Moves the ball across the screen according to parameters"""
        time.sleep(self.ball_speed)
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.x_move, y + self.y_move)

    def bounce(self):
        """Bounces the ball incase the ball hits the top or bottom walls"""
        self.y_move *= -1

    def change_direction(self):
        """Changes the ball direction in case the ball gets hit by one of the paddles"""
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.change_direction()
        self.ball_speed = 0.05

    def speed_up(self):
        self.ball_speed *= 0.9
