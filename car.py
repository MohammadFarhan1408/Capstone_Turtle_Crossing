from turtle import Turtle
import random

car_color = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
MOVE_DISTANCE = 10
MOVE_INCREASE_SPEED = 5


class Car:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE

    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(car_color))
            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREASE_SPEED

    def reset_cars(self):
        random_y = random.randint(-230, 230)
        for car in self.all_cars:
            car.goto(300, random_y)
