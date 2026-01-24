import turtle
from colorsys import hsv_to_rgb

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)

h = 0
alpha = 45
pensize = 1
for i in range(150):
    turtle.color(hsv_to_rgb(h,1,1))
    turtle.circle(i)
    turtle.right(alpha)
    h += 0.05

turtle.hideturtle()
turtle.done()