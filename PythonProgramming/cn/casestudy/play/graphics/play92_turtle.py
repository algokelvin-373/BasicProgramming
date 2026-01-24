import turtle
from colorsys import hsv_to_rgb

def draw_object(d, step):
    turtle.penup()
    turtle.right(30)
    turtle.forward(d)
    turtle.left(30)
    turtle.pendown()
    turtle.circle(d/2, 180, step)
    turtle.penup()
    turtle.left(30)
    turtle.forward(d)
    turtle.left(150)
    turtle.pendown()

turtle.bgcolor('black')
turtle.pensize(1)
turtle.speed(0)

h = 0
alpha = 30
w = 25
for i in range(3):
    steps = 3 + i
    for _ in range(int(360/alpha)):
        s = 25 + (100*i)
        for _ in range(5):
            turtle.color(hsv_to_rgb(h,1,1))
            draw_object(s, steps)
            s += 5
            h += 0.05
        turtle.left(alpha)

turtle.hideturtle()
turtle.done()