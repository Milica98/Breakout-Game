from turtle import Screen

from bricks import Bricks
from paddle import Paddle
from ball import Ball
import time

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

game_is_on = True

while game_is_on:
    time.sleep(0.05)

    # edges collision
    if ball.xcor() >= 290 or ball.xcor() <= -290:
        ball.change_x_direction()
    if ball.ycor() >= 290:
        ball.change_y_direction()
    elif ball.ycor() <= -280:
        game_is_on = False
        break

    # bricks collision

    for brick in bricks.bricks_array:
        if ball.distance(brick) <= 25:
            bricks.remove(brick)

    # paddle collision

    if ball.ycor() - 10 <= paddle.ycor() and ball.distance(paddle) <= 45:
        ball.change_y_direction()

    ball.move()
    screen.update()

screen.exitonclick()
