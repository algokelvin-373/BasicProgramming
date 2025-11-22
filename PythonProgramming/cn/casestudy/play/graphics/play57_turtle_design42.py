import turtle

def design3(x, y, xr, yr):
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

def design4(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

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

def design5(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    x_start = -x/2
    y_start = yr + -y/2
    x_finish = -x
    while x_start >= x_finish:
        s = abs(x_start + x_finish)
        turtle.penup()
        turtle.goto(xr + x_start, y_start)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(s)
            turtle.left(90)
        x_start -= 5
        y_start -= 5

def design42(s, pr, typ):
    for i in range(len(pr)):
        if typ[i] == 3:
            design3(s, s, pr[i][0], pr[i][1])
        elif typ[i] == 4:
            design4(s, s, pr[i][0], pr[i][1])
        elif typ[i] == 5:
            design5(s, s, pr[i][0], pr[i][1])

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
type_design = [3, 4, 5, 3, 4, 5, 3, 4, 5]

design42(data, pr_data, type_design)

turtle.hideturtle()
turtle.done()