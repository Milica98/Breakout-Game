from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 13, "normal")


class Scoreboard(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.__score = 0
        self.color("white")
        self.penup()
        self.goto(position_x, position_y)
        self.hideturtle()
        self.update_scoreboard()
        self.__start_position = (position_x, position_y)

    def update_scoreboard(self):
        self.write(f"Score: {self.__score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self, score):
        self.__score = score
        self.clear()
        self.update_scoreboard()

    def reset(self):
        self.goto(self.__start_position[0], self.__start_position[1])
        self.update_scoreboard()
