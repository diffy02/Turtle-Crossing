import turtle
import random

class Tree(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color((37,105,46))
        self.size = [0.4, 0.6, 0.75]
        self.tree_size = random.choice(self.size)

    def draw(self):
        self.fillcolor((37,105,46))
        self.begin_fill()
        for i in range(360):
            self.forward(self.tree_size)
            self.left(1)
        self.end_fill()
