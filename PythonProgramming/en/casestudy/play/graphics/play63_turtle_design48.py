import turtle

def design21(x, y, step, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.penup()
    turtle.goto(xr + -x, yr + y)
    turtle.pendown()
    radius = 0
    x_side = xr + -x
    y_side = yr + y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius)
        x_side += step
        y_side -= step
        if x_side >= xr + 0:
            radius -= 1
        else:
            radius += 1

    radius = 0
    x_side = xr + x
    y_side = yr + -y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius)
        x_side -= step
        y_side += step
        if x_side >= xr + 0:
            radius -= 1
        else:
            radius += 1

    radius = 0
    x_side = xr + -x
    y_side = yr + -y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius)
        x_side += step
        y_side += step
        if x_side <= xr + 0:
            radius -= 1
        else:
            radius += 1

    radius = 0
    x_side = xr + x
    y_side = yr + y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius)
        x_side -= step
        y_side -= step
        if x_side <= xr + 0:
            radius -= 1
        else:
            radius += 1

def design22(x, y, step, rad, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.penup()
    turtle.goto(xr + -x, yr + y)
    turtle.pendown()
    radius = 0
    x_side = xr + -x
    y_side = yr + y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius, rad)
        x_side += step
        y_side -= step
        if x_side >= xr + 0:
            radius -= 1
        else:
            radius += 1

    radius = 0
    x_side = xr + x
    y_side = yr + -y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius, rad)
        x_side -= step
        y_side += step
        if x_side >= xr + 0:
            radius -= 1
        else:
            radius += 1

    radius = 0
    x_side = xr + -x
    y_side = yr + -y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius, rad)
        x_side += step
        y_side += step
        if x_side <= xr + 0:
            radius -= 1
        else:
            radius += 1

    radius = 0
    x_side = xr + x
    y_side = yr + y
    for _ in range(int(side / step)):
        turtle.goto(x_side, y_side)
        turtle.circle(radius, rad)
        x_side -= step
        y_side -= step
        if x_side <= xr + 0:
            radius -= 1
        else:
            radius += 1

def design48(s, pr, typ):
    for i in range(len(pr)):
        if typ[i] == 21:
            design21(s, s, 5, pr[i][0], pr[i][1])
            turtle.setheading(0)
        elif typ[i] == 22:
            design22(s, s, 2, 90, pr[i][0], pr[i][1])
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
type_design = [21, 22, 21, 22, 21, 22, 21, 22, 21]

design48(data, pr_data, type_design)

turtle.hideturtle()
turtle.done()