from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(0, -250)
        self.move_step = (10, 10)

    def move(self):
        new_x = self.xcor() + self.move_step[0]
        new_y = self.ycor() + self.move_step[1]
        self.goto(new_x, new_y)

    def change_x_direction(self):
        self.move_step = (self.move_step[0] * -1, self.move_step[1])

    def change_y_direction(self):
        self.move_step = (self.move_step[0], self.move_step[1] * -1)

