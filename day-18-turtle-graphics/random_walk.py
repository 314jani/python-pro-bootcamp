from turtle import Turtle, Screen, color
import random


def random_hex_color():
    return "#" + "".join(random.choice("0123456789ABCDEF") for j in range(6))

directions = [0, 90, 180, 270]

t = Turtle()
t.shape("turtle")
t.pensize(10)
t.speed(0)

for i in range(300):
    t.color(random_hex_color())
    t.forward(20)
    t.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()