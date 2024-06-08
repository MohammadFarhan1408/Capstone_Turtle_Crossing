from turtle import Turtle, Screen
from animal import Animal
from car import Car
from level import Level
import time

screen = Screen()
screen.setup(width=600, height=500)
screen.tracer(0)

turtle = Animal()
cars = Car()
level = Level()

screen.listen()
screen.onkey(turtle.up, "Up")
screen.onkey(turtle.down, "Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            level.game_over()
            game_on = False

    if turtle.finish_line():
        turtle.restart_race()
        cars.level_up()
        level.increase_level()
        cars.reset_cars()
screen.exitonclick()
