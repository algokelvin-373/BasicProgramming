import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(1)
turtle.speed(0)

n = 20
x_start = 0
y_start = 0
side = 200
angle = 360 / n

turtle.goto(x_start, y_start)
for _ in range(n):
    turtle.forward(side)
    turtle.begin_fill()
    turtle.circle(2)
    turtle.end_fill()
    turtle.goto(x_start, y_start)
    turtle.left(angle)

turtle.hideturtle()
turtle.done()