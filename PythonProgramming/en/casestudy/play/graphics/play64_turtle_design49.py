import turtle

def design23(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.goto(xr + x, yr + y)
    turtle.goto(xr + x, yr + -y)
    turtle.goto(xr + -x, yr + y)

    x_start = xr + -x
    y_start = yr + y
    x_finish = xr + x
    y_finish = yr + -y
    x_side = xr + -x
    y_side = yr + -y
    for _ in range(int(side/10)):
        turtle.goto(x_start, y_start)
        turtle.goto(x_side, y_side)
        turtle.goto(x_finish, y_finish)
        x_side += 10
        y_side += 10

def design24(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.goto(xr + x, yr + -y)
    turtle.goto(xr + -x, yr + y)
    turtle.goto(xr + -x, yr + -y)
    turtle.goto(xr + x, yr + y)

    x_start = xr + x
    y_start = yr + y
    x_finish = xr + -x
    y_finish = yr + -y
    x_side = xr + x
    y_side = yr + -y
    for _ in range(int(side/10)):
        turtle.goto(x_start, y_start)
        turtle.goto(x_side, y_side)
        turtle.goto(x_finish, y_finish)
        x_side -= 10
        y_side += 10

def design25(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    x_start = xr + -x
    y_start = yr + -y
    x_finish = xr + x
    y_finish = yr + -y
    x_side = xr + 0
    y_side = yr + 0
    for _ in range(int(y/10)):
        turtle.goto(x_start, y_start)
        turtle.goto(x_side, y_side)
        turtle.goto(x_finish, y_finish)
        y_side -= 10

    x_start = xr + -x
    y_start = yr + y
    x_finish = xr + x
    y_finish = yr + y
    x_side = xr + 0
    y_side = yr + 0
    for _ in range(int(y / 10)):
        turtle.goto(x_start, y_start)
        turtle.goto(x_side, y_side)
        turtle.goto(x_finish, y_finish)
        y_side += 10

    x_start = xr + -x
    y_start = yr + y
    x_finish = xr + -x
    y_finish = yr + -y
    x_side = xr + 0
    y_side = yr + 0
    for _ in range(int(x / 10)):
        turtle.goto(x_start, y_start)
        turtle.goto(x_side, y_side)
        turtle.goto(x_finish, y_finish)
        x_side -= 10

    x_start = xr + x
    y_start = yr + y
    x_finish = xr + x
    y_finish = yr + -y
    x_side = xr + 0
    y_side = yr + 0
    for _ in range(int(x / 10)):
        turtle.goto(x_start, y_start)
        turtle.goto(x_side, y_side)
        turtle.goto(x_finish, y_finish)
        x_side += 10

def design49(s, pr, typ):
    for i in range(len(pr)):
        if typ[i] == 23:
            design23(s, s, pr[i][0], pr[i][1])
            turtle.setheading(0)
        elif typ[i] == 24:
            design24(s, s, pr[i][0], pr[i][1])
            turtle.setheading(0)
        elif typ[i] == 25:
            design25(s, s, pr[i][0], pr[i][1])
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
type_design = [23, 25, 24, 23, 25, 24, 23, 25, 24]

design49(data, pr_data, type_design)

turtle.hideturtle()
turtle.done()