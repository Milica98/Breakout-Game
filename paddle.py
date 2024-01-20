from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.color('white')
        self.penup()
        self.goto(position_x, position_y)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
