import turtle
import random

kolors = list(range(1,256))

class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()
        self.speed_value = 4
        self.chance = 40

    def creation(self,*args):
        if random.randint(1,self.chance) == 1:
            road_y = int(args[0])
            road_height = int(args[1])

            new_car = turtle.Turtle()
            new_car.hideturtle()
            new_car.shape('square')
            new_car.shapesize(stretch_len=1.5,stretch_wid=0.75)
            new_car.color((random.choice(kolors),random.choice(kolors),random.choice(kolors)))
            new_car.penup()
            new_car.setheading(0)
            spawn_car = random.randint(road_y,road_y + road_height)


            new_car.goto(450,spawn_car)
            new_car.showturtle()
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.backward(self.speed_value)

    def barrier(self):
        for car in self.car_list:
            if car.xcor() <= -400:
                car.hideturtle()
                self.car_list.remove(car)

    def collision(self,player):
        for car in self.car_list:
            if player.distance(car) < 25:
                return True

        return False