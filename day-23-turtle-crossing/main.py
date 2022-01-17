import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

garage = CarManager()

scoreboard = Scoreboard()
scoreboard.update_scoreboard()

game_is_on = True
counter = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if counter % 6 == 0:
        garage.start_car()
        
    garage.move_cars()
    
    # Detect collision with car
    for car in garage.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            
    # Detect turtle reaching top
    if player.ycor() > 280:
        player.back_to_start()
        garage.finish_reached()
        scoreboard.next_level()
    
    counter += 1

scoreboard.game_over()
screen.exitonclick()