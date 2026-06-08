import turtle
import random
kolors = list(range(1,256))

class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []

    def creation(self):
        new_car = turtle.Turtle()
        new_car.shapesize(stretch_len=1,stretch_wid=2)
        new_car.color(random.choice(kolors))
        self.car_list.append(new_car)