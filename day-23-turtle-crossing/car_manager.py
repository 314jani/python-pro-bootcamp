from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
TOP_LIMIT = 250
BOTTOM_LIMIT = -250
LEFT = 180
RIGHT = 0
STARTING_X = 300

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.hideturtle()
        
    
    def start_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.setheading(LEFT)
        car.shapesize(1, 2)
        random_y = random.randint(BOTTOM_LIMIT, TOP_LIMIT)
        car.goto(STARTING_X, random_y)
        self.all_cars.append(car)
        
    def move_cars(self):        
        for car in self.all_cars:
            car.forward(self.car_speed)
            
    def finish_reached(self):
        self.car_speed += MOVE_INCREMENT
        