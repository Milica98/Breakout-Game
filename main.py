from turtle import Screen

from bricks import Bricks
from paddle import Paddle
from ball import Ball
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
    for brick in bricks.bricks_array:
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

paddle = Paddle()
ball = Ball()
bricks = Bricks()

screen.listen()
screen.onkeypress(paddle.go_left, 'Left')
screen.onkeypress(paddle.go_right, 'Right')

while not is_game_over():
    time.sleep(0.05)

    collision_with_edges(ball)
    collision_with_bricks(ball, bricks)
    collision_with_paddle(ball, paddle)

    ball.move()
    screen.update()

screen.exitonclick()
