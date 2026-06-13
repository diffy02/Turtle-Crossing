import turtle
import random

kolors = list(range(1,256))

class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.truck_list = []
        self.hideturtle()
        self.speed_value1 = 4
        self.speed_value2 = 12
        self.chance1 = 45
        self.chance2 = 350

    def creation(self,*args):
        if random.randint(1,self.chance1) == 1:
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

            new_car.goto(450, spawn_car)
            new_car.showturtle()
            self.car_list.append(new_car)

        if random.randint(1,self.chance2) == 1:
            road_y = int(args[0])
            road_height = int(args[1])

            new_truck = turtle.Turtle()
            new_truck.hideturtle()
            new_truck.shape('square')
            new_truck.shapesize(stretch_len=3, stretch_wid=1)
            new_truck.color((191,107,76))
            new_truck.penup()
            new_truck.setheading(0)
            spawn_truck = random.randint(road_y,road_y + road_height)

            new_truck.goto(450, spawn_truck)
            new_truck.showturtle()
            self.truck_list.append(new_truck)


    def move1(self):
        for car in self.car_list:
            car.backward(self.speed_value1)

    def move2(self):
        for truck in self.truck_list:
            truck.backward(self.speed_value2)

    def barrier1(self):
        for car in self.car_list[:]:
            if car.xcor() <= -400:
                car.hideturtle()
                self.car_list.remove(car)

    def barrier2(self):
        for truck in self.truck_list[:]:
            if truck.xcor() <= -400:
                truck.hideturtle()
                self.truck_list.remove(truck)

    def collision(self,player):
        for car in self.car_list:
            if player.distance(car) < 25:
                return True

        return False