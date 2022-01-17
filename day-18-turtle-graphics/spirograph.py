from turtle import Turtle, Screen, color
import random


def random_hex_color():
    return "#" + "".join(random.choice("0123456789ABCDEF") for j in range(6))


t = Turtle()
t.shape("turtle")
t.pensize(1)
t.speed(0)

heading = 0

while heading <= 360:
    t.color(random_hex_color())
    t.circle(100)
    t.setheading(heading)
    heading += 10


screen = Screen()
screen.exitonclick()