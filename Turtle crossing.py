import turtle
import random
import time

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

move_loop1 = False
move_loop2 = False
def move_go():
    global move_loop1
    if not move_loop1:
        move_loop1 = True
        movement_up()

def move_stop():
    global move_loop1
    move_loop1 = False

def movement_up():
    if move_loop1:
        timmy.setheading(90)
        timmy.forward(5)
        screen.ontimer(movement_up,10)

def down_go():
    global move_loop2
    if not move_loop2:
        move_loop2 = True
        movement_down()

def down_stop():
    global move_loop2
    move_loop2 = False

def movement_down():
    if move_loop2:
        timmy.setheading(270)
        timmy.forward(5)
        screen.ontimer(movement_down,10)

screen.listen()
screen.onkeypress(move_go,'w')
screen.onkeyrelease(move_stop,'w')

screen.onkeypress(down_go,'s')
screen.onkeyrelease(down_stop,'s')

game = True
while game:
    screen.update()
    time.sleep(0.05)
turtle.done()

#test adding new code lines