import turtle
import time
import random
from Roads import Road
from Forest import Tree
from Cars import Car
from Collectible import Collect

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
timmy.goto(0,-325)

arrow = turtle.Turtle()
arrow.shape('arrow')
arrow.shapesize(stretch_wid=2,stretch_len=3)
arrow.color((255,158,26))
arrow.setheading(90)
arrow.penup()
arrow.goto(0,325)
arrow.hideturtle()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color((255,255,255))
writer.goto(0,10)
writer.write('hold q to turn left', align='center', font=("Courier New", 30, "bold"))
writer.goto(0,-30)
writer.write('hold e to turn right', align='center', font=("Courier New", 30, "bold"))
write_list = ['Game Over!','Unlucky...','Try again!']

counting = turtle.Turtle()
counting.hideturtle()
counting.penup()
counting.color((0,0,0))
counting.goto(270,310)

verdict = turtle.Turtle()
verdict.hideturtle()
verdict.penup()
verdict.color((53,76,188))
verdict.goto(0,100)

level = turtle.Turtle()
level.hideturtle()
level.penup()
level.color((245,143,42))
level.goto(-270,300)

food = turtle.Turtle()
food.penup()
food.goto(1000,1000)

base_speed = 2.5
move_loop1 = False
move_loop2 = False
turn = 3.5

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
        timmy.left(turn)
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
        timmy.right(turn)
        screen.ontimer(movement_down,10)

#####################################################

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
collect = Collect()

screen.listen()
screen.onkeypress(move_go, 'q')
screen.onkeyrelease(move_stop, 'q')

screen.onkeypress(down_go, 'e')
screen.onkeyrelease(down_stop, 'e')

start_intro = False
current_level = 1
last_speed_time1 = 0
last_speed_time2 = 0
counter = 0
counter_score = 0
requirement = 0
level.write(f'Level: {current_level}', align='center', font=("Verdana", 30, "normal"))
counting.write(f'{counter_score}', align='center', font=("Verdana", 25, "normal"))
switch = False
draw_once = True
game = True
while game:
    global speed_expiration, total_speed1, total_speed2
    screen.update()
    time.sleep(0.03)

    current_time1 = time.time()
    if current_time1 - last_speed_time1 >= 0.25:
        base_speed += 0.05
        last_speed_time1 = current_time1
    timmy.forward(base_speed)

    current_time2 = time.time()
    if current_time2 - last_speed_time2 >= 3:
        turn += 0.25
        last_speed_time2 = current_time2

    for road in road_list:
        cars.creation(road.ycor(),road.get_height())

    if current_level == 1:
        if timmy.ycor() > -340:
            if -250 <= timmy.ycor() <= -240:
                writer.clear()
                writer.goto(0,0)
                writer.write('Your speed gets faster \n as time passes', align='center', font=("Courier New", 30, "bold"))

            if -100 <= timmy.ycor() <= -90:
                writer.clear()
                writer.write('Cars and trucks \n gets faster the \n more levels you have completed', align='center',font=("Courier New", 20, "bold"))

            if timmy.ycor() >= 150:
                writer.clear()
                writer.write('then again, good luck!', align='center',font=("Courier New", 30, "bold"))

            if timmy.ycor() >= 250:
                writer.clear()

    if timmy.ycor() >= 375 and (requirement >= 4 or current_level == 1):
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

        for black_dots in collect.food_list:
            black_dots.clear()
            black_dots.hideturtle()

        road_list.clear()
        tree_list1.clear()
        tree_list2.clear()
        cars.car_list.clear()
        cars.truck_list.clear()
        collect.food_list.clear()
        cars = Car()

        collect.make()
        collect.position()
        timmy.goto(0, -325)
        base_speed = 2.5
        turn = 3.5
        requirement = 0

        total_speed1 = cars.speed_value1 + 0.75
        total_speed2 = cars.speed_value2 + 1.5
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

        if current_level % 3 == 0 and current_level < 10:
            additional_road = Road()
            additional_road.goto(-420, 0)
            additional_road.draw()
            road_list.append(additional_road)
            cars.speed_value1 *= 1.25
            cars.speed_value2 *= 1.25

        cars.speed_value1 *= 3
        cars.speed_value2 *= 3
        speed_expiration = time.time() + 2
        switch = True

#BARRIERS
#############################################################

    elif timmy.ycor() >= 375 and requirement < 4:
        timmy.sety(375)
        timmy.right(180)
        base_speed -= 2.25
    if timmy.ycor() <= -375:
        timmy.sety(-375)
        timmy.right(180)
        base_speed -= 2.25
    if timmy.xcor() <= -375:
        timmy.setx(-375)
        timmy.right(180)
        base_speed -= 2.25
    elif timmy.xcor() >= 375:
        timmy.setx(375)
        timmy.right(180)
        base_speed -= 2.25

#############################################################

    if switch and time.time() > speed_expiration:
        cars.speed_value1 = total_speed1 - 0.5
        cars.speed_value2 = total_speed2 - 1
        switch = False

    if cars.collision(timmy):
        game = False
        writer.clear()
        writer.goto(0,0)
        writer.color((216,72,101))
        writer.write(f'{random.choice(write_list)}', align='center',font=("Courier New", 45, "bold"))

    if current_level == 9 and draw_once:
        food.color((52, 94, 233))
        food.shape('circle')
        food.goto(0, 300)
        draw_once = False

    if collect.collide(timmy):
        counting.clear()
        counter += 1
        requirement += 1
        counter_score += 10
        counting.write(f'{counter_score}', align='center', font=("Verdana", 25, "normal"))

    if requirement == 4:
        arrow.showturtle()
    elif requirement < 4:
        arrow.hideturtle()

    if timmy.distance(food) < 15 and current_level == 9:
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
            if kars in screen.turtles():
                screen.turtles().remove(kars)

        level.clear()
        road_list.clear()
        tree_list1.clear()
        tree_list2.clear()
        cars.car_list.clear()
        food.hideturtle()
        timmy.hideturtle()
        writer.clear()
        counting.clear()
        screen.bgcolor((0,0,0))
        writer.goto(0,200)
        writer.color((255,255,255))
        writer.write('CONGRATULATIONS!', align='center',font=("Courier New", 60, "bold"))
        verdict.write('Final verdict...', align='center',font=("Courier New", 45, "bold"))
        verdict.goto(-50,-150)
        verdict.write(f'{counter} black dots eaten...', align='center',font=("Courier New", 45, "bold"))

    cars.move1()
    cars.move2()
    cars.barrier1()
    cars.barrier2()

turtle.done()
#test adding new code lines