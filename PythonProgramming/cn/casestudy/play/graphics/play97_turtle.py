import turtle
from colorsys import hsv_to_rgb

def design(alpha, scales):
    h = 0
    pensize = 1
    for i in range(100):
        if i % 25 == 0:
            pensize += 1
        turtle.color(hsv_to_rgb(h, 1, 1))
        turtle.pensize(pensize)
        turtle.forward(i * scales)
        turtle.right(alpha)
        h += 0.05
    turtle.goto(0, 0)
    turtle.clear()

turtle.bgcolor('black')
turtle.speed(0)

theta = 30
scale = 1
for _ in range(10):
    design(theta, scale)
    theta += 15
    scale += 1

turtle.hideturtle()
turtle.done()