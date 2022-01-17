from turtle import Turtle, Screen
import random
        

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Bet on your champion!", "Who will win the race?")
all_turtles = []
colors = ["red", "blue", "green", "yellow", "purple", "black"]
winning_color = "none"
y_position = -90
race_started = False
turtle_threads = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position)
    y_position += 30
    all_turtles.append(new_turtle)
    
if user_bet:    
    race_started = True
    
while race_started:
    for trtl in all_turtles:
        random_distance = random.randint(0, 20)
        trtl.forward(random_distance)
        
        if trtl.xcor() > 220:
            race_started = False
            winning_color = str(trtl.pencolor())
            break
        
print("The winner is " + winning_color + " turtle!")

if winning_color.lower() == user_bet.lower():
    print("You won!")
else:
    print("You lost!")

screen.exitonclick()