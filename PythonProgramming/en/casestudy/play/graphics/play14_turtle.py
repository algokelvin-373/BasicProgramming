import time
import turtle

def title(j):
    turtle.penup()
    turtle.goto(0, 225)
    turtle.write(
        f"n = {j}",
        align="center",
        font=("Arial", 16, "bold")
    )

def paint(n):
    for _ in range(n):
        for _ in range(6):
            turtle.forward(100)
            turtle.left(60)
        turtle.left(360 / n)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(1)
turtle.speed(100)

count = 21
for i in range(count):
    if i >= 3:
        title(i)
        turtle.goto(0, 0)
        turtle.pendown()
        paint(i)
    time.sleep(1)
    if i < count - 1:
        turtle.clear()

turtle.hideturtle()
turtle.done()