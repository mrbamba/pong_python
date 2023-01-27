from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Impact", 48, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """Initializes the Scoreboard object"""
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 240)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard to write to screen"""
        self.clear()
        self.write(arg=f"{self.left_score}    {self.right_score}", move=False, align=ALIGNMENT, font=FONT)

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()
