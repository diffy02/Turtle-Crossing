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
write_list = ['Game Over!','Unlucky...','Try again!']

level = turtle.Turtle()
level.hideturtle()
level.penup()
level.color((245,143,42))
level.goto(-270,300)
screen.update()

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
        timmy.forward(2.5)
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
        timmy.forward(2.5)
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

start_intro = False
current_level = 1
switch = True
level.write(f'Level: {current_level}', align='center', font=("Verdana", 30, "normal"))
game = True
while game:
    global additional_road
    screen.update()
    time.sleep(0.03)

    for road in road_list:
        cars.creation(road.ycor(),road.get_height())

    if current_level == 1:
        if timmy.ycor() > -340:
            if -250 <= timmy.ycor() <= -240:
                writer.clear()
                writer.goto(0,0)
                writer.write('Good job!', align='center', font=("Courier New", 30, "bold"))

            if -100 <= timmy.ycor() <= -90:
                writer.clear()
                writer.write('Cars go faster \n the more levels \n you have completed', align='center',font=("Courier New", 20, "bold"))

            if timmy.ycor() >= 150:
                writer.clear()
                writer.write('then again, good luck!', align='center',font=("Courier New", 30, "bold"))

            if timmy.ycor() >= 250:
                writer.clear()

    if timmy.ycor() >= 400:
        for road in road_list:
            road.clear()
            road.hideturtle()
            if road in screen.turtles():
                screen.turtles().remove(road)

        for tree in tree_list1 + tree_list2:
            tree.clear()
            tree.hideturtle()
            if tree in screen.turtles():
                screen.turtles().remove(tree)

        for kars in cars.car_list:
            kars.clear()
            kars.hideturtle()

        for truck in cars.truck_list:
            truck.clear()
            truck.hideturtle()

        road_list.clear()
        tree_list1.clear()
        tree_list2.clear()
        cars.car_list.clear()
        cars.truck_list.clear()
        cars = Car()

        timmy.goto(0, -350)

        cars.speed_value1 += 0.5
        cars.chance1 -= 1

        for a in range(max_road):
            new_road = Road()

            random_x1 = random.randint(-420, -420)
            random_y1 = road_place_y[a]

            new_road.goto(random_x1, random_y1)
            new_road.draw()
            road_list.append(new_road)

        tree_quantity1 = [10, 11, 12, 13, 14, 15]
        tree_list1 = []
        tree_list2 = []

        for b in range(random.choice(tree_quantity1)):
            new_tree = Tree()

            random_x2 = random.randint(-400, 400)
            random_y2 = random.randint(-375, -325)

            new_tree.penup()
            new_tree.goto(random_x2, random_y2)
            new_tree.pendown()
            new_tree.draw()
            tree_list1.append(new_tree)

        for c in range(random.choice(tree_quantity1)):
            new_tree = Tree()

            random_x2 = random.randint(-400, 400)
            random_y2 = random.randint(335, 375)

            new_tree.penup()
            new_tree.goto(random_x2, random_y2)
            new_tree.pendown()
            new_tree.draw()
            tree_list2.append(new_tree)

        level.clear()
        current_level += 1
        level.write(f'Level: {current_level}', align='center', font=("Verdana", 30, "normal"))

    if current_level % 3 == 0 and current_level < 10 and switch:
        switch = False
        additional_road = Road()
        additional_road.goto(-420, 0)
        additional_road.draw()
        road_list.append(additional_road)

    if cars.collision(timmy):
        game = False
        writer.clear()
        writer.goto(0,0)
        writer.color((216,72,101))
        writer.write(f'{random.choice(write_list)}', align='center',font=("Courier New", 45, "bold"))

    if current_level == 10:
        game = False
        for road in road_list:
            road.clear()
            road.hideturtle()
            if road in screen.turtles():
                screen.turtles().remove(road)

        for tree in tree_list1 + tree_list2:
            tree.clear()
            tree.hideturtle()
            if tree in screen.turtles():
                screen.turtles().remove(tree)

        for kars in cars.car_list:
            kars.clear()
            kars.hideturtle()

        level.clear()
        road_list.clear()
        tree_list1.clear()
        tree_list2.clear()
        cars.car_list.clear()
        writer.clear()
        screen.bgcolor((0,0,0))
        writer.goto(0,0)
        writer.color((255,255,255))
        writer.write('CONGRATULATIONS! \n you are truly a \n certified turtle crosser', align='center',font=("Courier New", 30, "bold"))

    cars.move1()
    cars.move2()
    cars.barrier1()
    cars.barrier2()

turtle.done()
#test adding new code lines