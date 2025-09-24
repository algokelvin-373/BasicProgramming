import turtle

def design21(x, y, step, rad):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.penup()
    turtle.goto(-x, y)
    turtle.pendown()
    radius = 0
    x_side = -x
    y_side = y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius, rad)
        x_side += step
        y_side -= step
        if x_side >= 0:
            radius -= 1
        else:
            radius += 1

    radius = 0
    x_side = x
    y_side = -y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius, rad)
        x_side -= step
        y_side += step
        if x_side >= 0:
            radius -= 1
        else:
            radius += 1

    radius = 0
    x_side = -x
    y_side = -y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius, rad)
        x_side += step
        y_side += step
        if x_side <= 0:
            radius -= 1
        else:
            radius += 1

    radius = 0
    x_side = x
    y_side = y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius, rad)
        x_side -= step
        y_side -= step
        if x_side <= 0:
            radius -= 1
        else:
            radius += 1

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

design21(200, 200, 2, 90)

turtle.hideturtle()
turtle.done()