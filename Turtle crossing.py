import turtle
import time
import random
from Roads import Road
from Forest import Tree
from Cars import Car

screen = turtle.Screen()
turtle.colormode(255)
screen.setup(width=750,height=750)
screen.bgcolor((83,235,104))
screen.tracer(0)

timmy = turtle.Turtle()
timmy.shape('turtle')
timmy.color((37,105,46))
timmy.setheading(90)
timmy.penup()
timmy.goto(0,-350)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color((255,255,255))
writer.goto(0,10)
writer.write('hold w to go up', align='center', font=("Courier New", 30, "bold"))
writer.goto(0,-30)
writer.write('hold s to go down', align='center', font=("Courier New", 30, "bold"))

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



max_road = 2
road_list = []
road_place_y = [175,-175]
for a in range(max_road):
    new_road = Road()

    random_x1 = random.randint(-420,-420)
    random_y1 = road_place_y[a]

    new_road.goto(random_x1, random_y1)
    new_road.draw()
    road_list.append(new_road)

tree_quantity1 = [10,11,12,13,14,15]
tree_list1 = []
tree_list2 = []

for b in range(random.choice(tree_quantity1)):
    new_tree = Tree()

    random_x2 = random.randint(-400,400)
    random_y2 = random.randint(-375,-325)

    new_tree.penup()
    new_tree.goto(random_x2, random_y2)
    new_tree.pendown()
    new_tree.draw()
    tree_list1.append(new_tree)

for c in range(random.choice(tree_quantity1)):
    new_tree = Tree()

    random_x2 = random.randint(-400,400)
    random_y2 = random.randint(335,375)

    new_tree.penup()
    new_tree.goto(random_x2, random_y2)
    new_tree.pendown()
    new_tree.draw()
    tree_list2.append(new_tree)

cars = Car()

screen.listen()
screen.onkeypress(move_go, 'w')
screen.onkeyrelease(move_stop, 'w')

screen.onkeypress(down_go, 's')
screen.onkeyrelease(down_stop, 's')

game = True
while game:
    screen.update()
    time.sleep(0.05)
    for road in road_list:
        cars.creation(road.ycor(),road.get_height())

    if timmy.ycor() == -250:
        writer.clear()
        writer.write('Good job lol', align='center', font=("Courier New", 30, "bold"))

    if timmy.ycor() == -100:
        writer.clear()
        writer.write('More cars spawns \n the more levels you have completed', align='center',font=("Courier New", 20, "bold"))

    if timmy.ycor() == 150:
        writer.clear()
        writer.write('then again, good luck!', align='center',font=("Courier New", 30, "bold"))

    if timmy.ycor() == 250:
        writer.clear()

    cars.move()
    cars.barrier()

turtle.done()
#test adding new code lines