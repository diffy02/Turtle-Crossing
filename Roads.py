import turtle
import random

pixels = [80, 90, 100, 120, 150]

class Road(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color((164, 164, 164))
        self.penup()  # Keep the pen up while initializing and moving
        # Moving 'pick' inside __init__ ensures each road can have a UNIQUE width!
        self.pick = random.choice(pixels)

    def draw(self):
        self.pendown()  # Put the pen down only to draw the road shape
        self.fillcolor((164, 164, 164))
        self.begin_fill()
        for i in range(2):
            self.forward(900)
            self.left(90)
            self.forward(self.pick)
            self.left(90)
        self.end_fill()
        self.penup()