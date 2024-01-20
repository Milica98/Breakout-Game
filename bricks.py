from turtle import Turtle


def get_new_brick(color, position):
    brick = Turtle()
    brick.shape('square')
    brick.shapesize(stretch_wid=1, stretch_len=2)
    brick.color(color)
    brick.penup()
    brick.goto(position)
    return brick


class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.__bricks_array = []
        self.__initialize()

    def __initialize(self):
        self.__initial_number = 13 * 4
        for i in range(0, 13):
            new_brick = get_new_brick('yellow', (267 + -45 * i, 100))
            self.__bricks_array.append(new_brick)
            new_brick = get_new_brick('green', (267 + -45 * i, 125))
            self.__bricks_array.append(new_brick)
            new_brick = get_new_brick('orange', (267 + -45 * i, 150))
            self.__bricks_array.append(new_brick)
            new_brick = get_new_brick('red', (267 + -45 * i, 175))
            self.__bricks_array.append(new_brick)

    def remove(self, brick):
        brick.reset()
        self.__bricks_array.remove(brick)

    def get_initial_number(self):
        return self.__initial_number

    def get_broken_number(self):
        return self.get_initial_number() - self.get_current_number()

    def get_current_number(self):
        return len(self.__bricks_array)

    def get_bricks(self):
        return self.__bricks_array
