import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car:
    def __init__(self, speed):
        self.turtle = Turtle("square")
        self.turtle.color(random.choice(COLORS))
        self.turtle.shapesize(stretch_wid=1, stretch_len=2)
        self.turtle.penup()
        self.turtle.goto(300-40, random.randint(-260, 260))
        self.turtle.setheading(180)
        self.speed = speed

    def move(self):
        self.turtle.forward(self.speed)

    def update_speed(self, speed):
        self.speed = speed

class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 3:
            self.cars.append(Car(self.speed))

    def move_cars(self):
        for car in self.cars:
            car.move()

    def check_collision_with_player(self, player):
        for car in self.cars:
            if car.turtle.distance(player.turtle) <= 20:
                return True
        return False

    def update_cars_speed(self):
        self.speed += MOVE_INCREMENT
        for car in self.cars:
            car.update_speed(self.speed)
