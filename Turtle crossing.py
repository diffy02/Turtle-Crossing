import turtle
import random

screen = turtle.Screen()
turtle.colormode(255)
screen.bgcolor((83,235,104))
screen.tracer(0)

timmy = turtle.Turtle()
timmy.shape('turtle')
timmy.color((37,105,46))
timmy.setheading(90)
timmy.penup()
timmy.goto(0,-350)

screen.update()
turtle.done()