import turtle
from colorsys import hsv_to_rgb

def draw_object(d):
    turtle.right(45)
    turtle.circle(d, 90)
    turtle.left(90)
    turtle.circle(d, 90)
    turtle.right(-135)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.pensize(1)
turtle.speed(0)

h = 0
alpha = 45
for _ in range(int(360 / alpha)):
    s = 10
    for _ in range(15):
        turtle.color(hsv_to_rgb(h, 1, 1))
        draw_object(s)
        h += 0.05
        s += 10
    turtle.right(alpha)

turtle.hideturtle()
turtle.done()