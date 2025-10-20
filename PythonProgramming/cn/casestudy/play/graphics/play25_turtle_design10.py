import turtle

def design10(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    x_start = -x
    y_start = y
    x_finish = x
    y_finish = -y
    turtle.penup()
    turtle.goto(x_start, y_start)
    turtle.pendown()

    x1 = x_start
    y1 = y_start
    x2 = x_start
    y2 = y_start
    while y1 >= y_finish:
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)
        y1 -= 10
        x2 += 10
    y1 += 10
    x2 -= 10
    while x1 <= x_finish:
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)
        x1 += 10
        y2 -= 10

    x_start = x
    y_start = y
    x_finish = -x
    y_finish = -y
    turtle.penup()
    turtle.goto(x_start, y_start)
    turtle.pendown()

    x1 = x_start
    y1 = y_start
    x2 = x_start
    y2 = y_start
    while y1 >= y_finish:
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)
        y1 -= 10
        x2 -= 10
    y1 += 10
    x2 += 10
    while x1 >= x_finish:
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)
        x1 -= 10
        y2 -= 10

    radius = x
    turtle.color('salmon', 'black')
    while radius >= 50:
        turtle.penup()
        turtle.goto(0, -radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius, steps=4)
        turtle.end_fill()
        radius -= 10

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

design10(200, 200)

turtle.hideturtle()
turtle.done()