import turtle
import random

pixels = [90, 100, 120, 150]

class Road(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color((164, 164, 164))
        self.penup()
        self.pick = random.choice(pixels)

    def draw(self):
        self.pendown()
        self.fillcolor((164, 164, 164))
        self.begin_fill()
        for a in range(2):
            self.forward(900)
            self.left(90)
            self.forward(self.pick)
            self.left(90)
        self.end_fill()
        self.penup()

    def get_height(self):
        return self.pick