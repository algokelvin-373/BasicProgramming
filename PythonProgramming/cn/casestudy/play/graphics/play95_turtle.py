import turtle
from colorsys import hsv_to_rgb

def draw(s):
    turtle.right(45)
    turtle.circle(s * 2, 90)
    turtle.left(90)
    turtle.circle(s * 2, 90)
    turtle.right(-135)

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)

h = 0
alpha = 45
pensize = 1
for i in range(150):
    turtle.color(hsv_to_rgb(h,1,1))
    draw(i)
    turtle.right(alpha)
    h += 0.05

turtle.hideturtle()
turtle.done()