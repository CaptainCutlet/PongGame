from screen import MainScreen
from paddle import Paddle
from turtle import Screen
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.setup(height=800, width=1000)
screen.bgcolor("black")
screen.tracer(0)

screen_elements = MainScreen()

r_paddle = Paddle(470)
l_paddle = Paddle(-480)

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

ball = Ball()

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move_ball()

    # Detect collision with top or bottom walls
    if ball.ycor() > 390 or ball.ycor() < -380:
        ball.bounce()

    # Detect collision with a paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 440) or (ball.distance(l_paddle) < 50 and ball.xcor() < -450):
        ball.bounce_off_a_paddle()

    if ball.xcor() > 500:
        screen_elements.clear()
        screen_elements.add_to_left()
        ball.reset_position()

    if ball.xcor() < -490:
        screen_elements.clear()
        screen_elements.add_to_right()
        ball.reset_position()


screen.exitonclick()
