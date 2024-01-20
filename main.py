from turtle import Screen

from bricks import Bricks
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time


def is_game_over() -> bool:
    if ball.ycor() <= -280:
        return True
    return False


def collision_with_edges(ball):
    if ball.xcor() >= 290 or ball.xcor() <= -290:
        ball.change_x_direction()
    if ball.ycor() >= 290:
        ball.change_y_direction()


def collision_with_bricks(ball, bricks):
    for brick in bricks.get_bricks():
        if ball.distance(brick) <= 25:
            bricks.remove(brick)


def collision_with_paddle(ball, paddle):
    if ball.ycor() - 10 <= paddle.ycor() and ball.distance(paddle) <= 45:
        ball.change_y_direction()


screen = Screen()

screen.setup(width=600, height=600)
screen.title('Breakout Game')
screen.bgcolor('black')
screen.tracer(0)

paddle = Paddle(position_x=0, position_y=-280)
ball = Ball(position_x=0, position_y=-250)
bricks = Bricks()
scoreboard = Scoreboard(position_x=220, position_y=270)

screen.listen()
screen.onkeypress(paddle.go_left, 'Left')
screen.onkeypress(paddle.go_right, 'Right')

while not is_game_over():
    time.sleep(0.03)

    collision_with_edges(ball)
    collision_with_bricks(ball, bricks)
    collision_with_paddle(ball, paddle)

    ball.move()
    screen.update()
    scoreboard.update_score(
        bricks.get_initial_number() - bricks.get_current_number())

screen.exitonclick()
