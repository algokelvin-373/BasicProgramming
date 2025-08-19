import turtle
import math

def draw_oval(a, b):
    turtle.penup()
    turtle.goto(a, 0)
    turtle.pendown()

    turtle.setheading(0)
    for i in range(101):
        t = i * 2 * math.pi / 100  # parameter t from 0 to 2π
        x = a * math.cos(t)
        y = b * math.sin(t)
        turtle.goto(x, y)

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(0)

draw_oval(100, 50)

turtle.hideturtle()
turtle.done()