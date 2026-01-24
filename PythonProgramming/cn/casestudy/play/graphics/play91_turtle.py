import turtle
from colorsys import hsv_to_rgb

def object1(d1):
    turtle.penup()
    turtle.right(30)
    turtle.forward(d1)
    turtle.pendown()
    turtle.left(60)
    turtle.forward(d1)
    turtle.left(120)
    turtle.forward(d1)
    turtle.left(60)
    turtle.penup()
    turtle.forward(d1)
    turtle.left(150)
    turtle.pendown()

def object2(d2):
    turtle.penup()
    turtle.right(30)
    turtle.forward(d2)
    turtle.pendown()
    turtle.left(30)
    turtle.circle(d2 / 2, 180)
    turtle.penup()
    turtle.left(30)
    turtle.forward(d2)
    turtle.left(150)
    turtle.pendown()

def draw_object(d, theta):
    for _ in range(int(360 / theta)):
        if i % 2 == 1:
            object2(d)
        else:
            object1(d)
        turtle.left(theta)

turtle.bgcolor('black')
turtle.pensize(1)
turtle.speed(0)

s = 10
t = 0
h = 0
alpha = 30
times = 8
for i in range(times):
    turtle.color(hsv_to_rgb(h, 1, 1))
    draw_object(s, alpha)
    if (i+1) % 2 == 0:
        t += 5
    s += (25 + t)
    h += 0.075

turtle.hideturtle()
turtle.done()