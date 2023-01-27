from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        """Receives initial paddle position and initials the Paddle object"""
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        """Moves the paddle up within game bounds"""
        if 250 > self.ycor():
            x = self.xcor()
            y = self.ycor()
            self.goto(x, y+20)

    def down(self):
        """Moves the paddle down within game bounds"""
        if self.ycor() > -240:
            x = self.xcor()
            y = self.ycor()
            self.goto(x, y-20)
