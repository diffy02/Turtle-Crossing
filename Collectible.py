import turtle
import random

random_food = [5,6,7,8]
class Collect(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.food_list = []
        self.hideturtle()

    def make(self):
        for i in range(random.choice(random_food)):
            new_food = turtle.Turtle()
            new_food.hideturtle()
            new_food.penup()
            new_food.color('black')
            new_food.shape('circle')
            new_food.shapesize(stretch_len=0.5,stretch_wid=0.5)
            new_food.showturtle()
            self.food_list.append(new_food)

    def position(self):
        for yummy in self.food_list:
            yummy.goto(random.randint(-250,300),random.randint(-250,300))

    def collide(self,player):
        for food in self.food_list:
            if food.distance(player) < 11:
                food.hideturtle()
                self.food_list.remove(food)
                return True
        return False