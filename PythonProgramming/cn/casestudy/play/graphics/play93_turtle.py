import turtle
from colorsys import hsv_to_rgb

turtle.bgcolor('black')
turtle.speed(0)

h = 0
alpha = 60
pensize = 1
for i in range(100):
    if i % 20 == 0:
        pensize += 2
    turtle.color(hsv_to_rgb(h,1,1))
    turtle.pensize(pensize)
    turtle.forward(i * 4)
    turtle.right(alpha)
    h += 0.05

turtle.hideturtle()
turtle.done()