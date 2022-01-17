from turtle import Turtle, xcor

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 5)
        self.setheading(UP)
        self.goto(position)
        
    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def go_up(self):
        self.setheading(UP)
        
        if self.ycor() < 300: 
            self.move_player()

    def go_down(self):
        self.setheading(DOWN)
        
        if self.ycor() > -300: 
            self.move_player()
