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
screen.onkey(player.up, "Up")

car_manager = CarManager()
car_manager.hideturtle()

scoreboard = Scoreboard()
scoreboard.hideturtle()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.drive()

    # detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish():
        # turtle at start, make cars go faster
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()

    screen.update()

screen.exitonclick()
