from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
DOWN = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(UP)
        self.goto(STARTING_POSITION)
        
    def move_up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)
    
    def move_down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)
        
    def back_to_start(self):
        self.goto(STARTING_POSITION)