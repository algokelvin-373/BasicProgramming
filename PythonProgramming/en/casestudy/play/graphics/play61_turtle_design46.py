import turtle

def design13(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.goto(xr + -x, yr + -y)
    turtle.left(90)

    radius = 0
    x_side = xr + -x
    y_side = yr + -y
    while x_side <= xr + x:
        turtle.circle(radius, 90)
        x_side += 10
        turtle.penup()
        turtle.goto(x_side, y_side)
        turtle.pendown()
        turtle.left(-90)
        radius += 10
    x_side -= 10
    radius -= 10
    while y_side <= yr + y:
        turtle.penup()
        turtle.goto(x_side, y_side)
        turtle.pendown()
        turtle.circle(radius, 90)
        y_side += 30
        turtle.left(-90)
        radius -= 30

def design14(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.penup()
    turtle.goto(xr + x,yr + y)
    turtle.pendown()

    turtle.right(90)

    radius = 0
    x_side = xr + x
    y_side = yr + y
    while x_side >= xr + -x:
        turtle.circle(radius, 90)
        x_side -= 10
        turtle.penup()
        turtle.goto(x_side, y_side)
        turtle.pendown()
        turtle.left(-90)
        radius += 10
    x_side += 10
    radius -= 10
    while y_side >= yr + -y:
        turtle.penup()
        turtle.goto(x_side, y_side)
        turtle.pendown()
        turtle.circle(radius, 90)
        y_side -= 30
        turtle.left(-90)
        radius -= 30

def design15(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.goto(xr + x, yr + -y)
    turtle.left(90)

    radius = side
    x_side = xr + x
    y_side = yr + -y
    while y_side <= yr + y:
        turtle.circle(radius, 90)
        y_side += 20
        turtle.left(-90)
        radius -= 20
        turtle.penup()
        turtle.goto(x_side, y_side)
        turtle.pendown()

    turtle.penup()
    turtle.goto(xr + -x, yr + y)
    turtle.pendown()
    turtle.right(180)

    radius = side
    x_side = xr + -x
    y_side = yr + y
    while y_side >= yr + -y:
        turtle.circle(radius, 90)
        y_side -= 20
        turtle.left(-90)
        radius -= 20
        turtle.penup()
        turtle.goto(x_side, y_side)
        turtle.pendown()

    turtle.penup()
    turtle.goto(xr + -x, yr + y)
    turtle.pendown()
    turtle.right(-45)
    radius = 0
    x_side = xr + -x
    y_side = yr + y
    step = 4
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius)
        x_side += step
        y_side -= step
        if x_side >= xr + 0:
            radius -= 1
        else:
            radius += 1

    turtle.penup()
    turtle.goto(xr + x, yr + -y)
    turtle.pendown()
    turtle.left(180)
    radius = 0
    x_side = xr + x
    y_side = yr + -y
    step = 4
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius)
        x_side -= step
        y_side += step
        if x_side <= xr + 0:
            radius -= 1
        else:
            radius += 1

def design46(s, pr, typ):
    for i in range(len(pr)):
        if typ[i] == 13:
            design13(s, s, pr[i][0], pr[i][1])
            turtle.setheading(0)
        elif typ[i] == 14:
            design14(s, s, pr[i][0], pr[i][1])
            turtle.setheading(0)
        elif typ[i] == 15:
            design15(s, s, pr[i][0], pr[i][1])
            turtle.setheading(0)

turtle.setup(width=650, height=650)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

data = 100
pr_data = [
    (-200, 200),
    (0, 200),
    (200, 200),
    (-200, 0),
    (0, 0),
    (200, 0),
    (-200, -200),
    (0, -200),
    (200, -200),
]
type_design = [15, 14, 13, 13, 15, 14, 14, 13, 15]

design46(data, pr_data, type_design)

turtle.hideturtle()
turtle.done()