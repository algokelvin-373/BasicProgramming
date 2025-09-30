import turtle

def design8(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()

    space = 0
    while space <= side:
        radius = side - space
        if space == 0:
            turtle.begin_fill()
        turtle.forward(space)
        turtle.circle(radius, 90)
        turtle.forward(space)
        turtle.right(270)
        turtle.forward(space)
        turtle.circle(radius, 90)
        turtle.forward(space)
        turtle.right(-90)
        if space == 0:
            turtle.end_fill()
        space += 30

def design9(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.penup()
    turtle.goto(xr + x, yr + -y)
    turtle.pendown()

    space = 0
    while space <= side:
        radius = side - space
        if space == 0:
            turtle.begin_fill()
        turtle.backward(space)
        turtle.circle(radius, -90)
        turtle.backward(space)
        turtle.left(270)
        turtle.backward(space)
        turtle.circle(radius, -90)
        turtle.backward(space)
        turtle.left(-90)
        if space == 0:
            turtle.end_fill()
        space += 30

def design10(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    x_start = xr + -x
    y_start = yr + y
    x_finish = xr + x
    y_finish = yr + -y
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

    x_start = xr + x
    y_start = yr + y
    x_finish = xr + -x
    y_finish = yr + -y
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
        turtle.goto(xr + 0, yr + -radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius, steps=4)
        turtle.end_fill()
        radius -= 10

def design44(s, pr, typ):
    for i in range(len(pr)):
        if typ[i] == 8:
            design8(s, s, pr[i][0], pr[i][1])
        elif typ[i] == 9:
            design9(s, s, pr[i][0], pr[i][1])
        elif typ[i] == 10:
            design10(s, s, pr[i][0], pr[i][1])

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
type_design = [8, 9, 8, 9, 8, 9, 8, 9, 8]

design44(data, pr_data, type_design)

turtle.hideturtle()
turtle.done()