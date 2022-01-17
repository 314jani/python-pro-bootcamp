from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

POS_LEFT = (-550, 0)
POS_RIGHT = (550, 0)

screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_left = Paddle(POS_LEFT)
paddle_right = Paddle(POS_RIGHT)

screen.listen()
screen.onkey(paddle_left.go_up, ("W"))
screen.onkey(paddle_left.go_up, ("w"))
screen.onkey(paddle_left.go_down, "S")
screen.onkey(paddle_left.go_down, "s")
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

game_on = True

while game_on:
    ball.move()
    screen.update()
    time.sleep(ball.ball_speed)
    
    # Detect collision with up and down wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()
        
    # Detect collision with paddles
    if ((ball.distance(paddle_right) < 50 and ball.xcor() > 520) or (ball.distance(paddle_left) < 50 and ball.xcor() < -520)):
        ball.bounce_x()
        
        
    # Detect right paddle miss
    if ball.xcor() > 550:
        ball.reset_position()
        scoreboard.point_right()
    
    # Detect left paddle miss
    if ball.xcor() < -550:
        ball.reset_position()
        scoreboard.point_left()
        
screen.exitonclick()
