import turtle
from colorsys import hsv_to_rgb

def draw_object(d):
    turtle.right(30)
    turtle.forward(d)
    turtle.left(30)
    turtle.circle(d / 2, 180)
    turtle.left(30)
    turtle.forward(d)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('white')
turtle.pensize(1)
turtle.speed(0)


h = 0
alpha = 45
for _ in range(int(360 / alpha)):
    s = 10
    for _ in range(15):
        turtle.color(hsv_to_rgb(h, 1, 1))
        draw_object(s)
        turtle.left(150)
        h += 0.05
        s += 10
    turtle.right(alpha)


turtle.hideturtle()
turtle.done()