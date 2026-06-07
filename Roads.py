import turtle
import random
pixels = [60,70,80,90]

turtle.colormode(255)
pick = random.choice(pixels)
class Road(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color((164,164,164))
        self.penup()
        self.goto(-420,0)
        self.pendown()

    def draw(self):
        self.fillcolor((164,164,164))
        self.begin_fill()
        for i in range(2):
            self.forward(900)
            self.left(90)
            self.forward(pick)
            self.left(90)

        self.end_fill()
