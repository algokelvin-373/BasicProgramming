import time
import turtle

def circle_design(n, side):
    turtle.penup()
    turtle.goto(0, 225)
    turtle.write(
        f"n = {n}",
        align="center",
        font=("Arial", 16, "bold")
    )
    turtle.pendown()

    turtle.goto(0, 0)

    angle = 10
    color = 250
    for _ in range(int(360/angle)):
        turtle.circle(side, steps=n)
        turtle.left(angle)
    turtle.clear()

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(1)
turtle.speed(0)

for i in range(21):
    if i < 3:
        continue
    circle_design(i, 100)

turtle.hideturtle()
turtle.done()