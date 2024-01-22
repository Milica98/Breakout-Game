from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(position_x, position_y)
        self.__move_step = (10, 10)
        self.__start_position = (position_x, position_y)

    def move(self):
        new_x = self.xcor() + self.__move_step[0]
        new_y = self.ycor() + self.__move_step[1]
        self.goto(new_x, new_y)

    def change_x_direction(self):
        self.__move_step = (self.__move_step[0] * -1, self.__move_step[1])

    def change_y_direction(self):
        self.__move_step = (self.__move_step[0], self.__move_step[1] * -1)

    def reset(self):
        self.goto(self.__start_position[0], self.__start_position[1])
