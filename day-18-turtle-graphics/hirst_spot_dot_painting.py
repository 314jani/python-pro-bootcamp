import colorgram
from turtle import Turtle, Screen
import random


screen = Screen()
screen.colormode(255)
t = Turtle()
t.speed(0)
t.penup()
t.hideturtle()

color_palette = colorgram.extract("ironman.jpg", 10)
rgb_colors = []
number_dots = 100

for color in color_palette:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    new_color = (red, green, blue)
    
    if red > 220 and green > 220 and blue > 220:
        continue
    if red < 120 and green < 120 and blue < 120:
        continue
    
    rgb_colors.append(new_color)
    
print(rgb_colors)

t.setheading(225)
t.forward(300)
t.setheading(0)

for dot_count in range(1, number_dots + 1):
    t.color(random.choice(rgb_colors))
    t.dot(20)
    t.forward(50)
    
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
        
screen.exitonclick()