from turtle import Turtle, Screen


def move_forward():
    t.forward(10)
    
    
def move_backward():
    t.back(10)
    
    
def turn_left():
    t.left(15)
    

def turn_right():
    t.right(15)
    
    
def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    

t = Turtle()
screen = Screen()

screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_backward, "Down")
screen.onkey(clear_screen, "c")

screen.exitonclick()