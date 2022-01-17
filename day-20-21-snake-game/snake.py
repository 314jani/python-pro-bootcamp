from turtle import Turtle

STARTING_POSITIONS = ((0, 0), (0, 20), (0, 40))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        segment.speed(0)
        self.segments.append(segment)

    def grow(self):
        position = self.segments[-1].position()
        self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_right(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
