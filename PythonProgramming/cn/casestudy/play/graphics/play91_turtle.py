import turtle
from colorsys import hsv_to_rgb

def object1(d1):
    turtle.right(30)
    turtle.forward(d1)
    turtle.left(60)
    turtle.forward(d1)
    turtle.left(120)
    turtle.forward(d1)
    turtle.left(60)
    turtle.forward(d1)
    turtle.left(150)

def object2(d2):
    turtle.right(30)
    turtle.forward(d2)
    turtle.left(30)
    turtle.circle(d2 / 2, 180)
    turtle.left(30)
    turtle.forward(d2)
    turtle.left(150)

def object3(d3):
    turtle.right(45)
    turtle.circle(d3, 90)
    turtle.left(90)
    turtle.circle(d3, 90)
    turtle.right(-135)

def draw_object(d, theta):
    for _ in range(int(360 / theta)):
        if i % 3 == 1:
            object2(d)
        elif i % 3 == 2:
            object3(d)
        else:
            object1(d)
        turtle.left(theta)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.pensize(1)
turtle.speed(0)

s = 10
# t = 5
h = 0
alpha = 30
times = 9
for i in range(times):
    turtle.color(hsv_to_rgb(h, 1, 1))
    draw_object(s, alpha)
    # if (i+1) % 3 == 0:
    #     t += 15
    # s += t
    s += 5
    h += 0.075

turtle.hideturtle()
turtle.done()