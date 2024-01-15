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
        self.bricks_array = []
        self.initialize()

    def initialize(self):
        for i in range(0, 13):
            new_brick = get_new_brick('yellow', (267 + -45 * i, 100))
            self.bricks_array.append(new_brick)
            new_brick = get_new_brick('green', (267 + -45 * i, 125))
            self.bricks_array.append(new_brick)
            new_brick = get_new_brick('orange', (267 + -45 * i, 150))
            self.bricks_array.append(new_brick)
            new_brick = get_new_brick('red', (267 + -45 * i, 175))
            self.bricks_array.append(new_brick)

    def remove(self, brick):
        brick.reset()
        self.bricks_array.remove(brick)
