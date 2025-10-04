import turtle

def design15(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.goto(x,-y)
    turtle.left(90)

    radius = side
    x_side = x
    y_side = -y
    while y_side <= y:
        turtle.circle(radius, 90)
        y_side += 20
        turtle.left(-90)
        radius -= 20
        turtle.penup()
        turtle.goto(x_side, y_side)
        turtle.pendown()

    turtle.penup()
    turtle.goto(-x, y)
    turtle.pendown()
    turtle.right(180)

    radius = side
    x_side = -x
    y_side = y
    while y_side >= -y:
        turtle.circle(radius, 90)
        y_side -= 20
        turtle.left(-90)
        radius -= 20
        turtle.penup()
        turtle.goto(x_side, y_side)
        turtle.pendown()

    turtle.penup()
    turtle.goto(-x, y)
    turtle.pendown()
    turtle.right(-45)
    radius = 0
    x_side = -x
    y_side = y
    step = 4
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius)
        x_side += step
        y_side -= step
        if x_side >= 0:
            radius -= 1
        else:
            radius += 1

    turtle.penup()
    turtle.goto(x, -y)
    turtle.pendown()
    turtle.left(180)
    radius = 0
    x_side = x
    y_side = -y
    step = 4
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius)
        x_side -= step
        y_side += step
        if x_side <= 0:
            radius -= 1
        else:
            radius += 1

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

design15(200, 200)

turtle.hideturtle()
turtle.done()