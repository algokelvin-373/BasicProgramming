import turtle

def design11(x, y, xr, yr):
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

    x1  = x_start
    while x1 < x_finish:
        turtle.penup()
        turtle.goto(x1, y_start)
        turtle.pendown()
        turtle.goto(x1, y_finish)
        x1 += 5

def design12(x, y, xr, yr):
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

    y1 = y_start
    while y1 > y_finish:
        turtle.penup()
        turtle.goto(x_start, y1)
        turtle.pendown()
        turtle.goto(x_finish, y1)
        y1 -= 5

def design45(s, pr, typ):
    for i in range(len(pr)):
        if typ[i] == 11:
            design11(s, s, pr[i][0], pr[i][1])
        elif typ[i] == 12:
            design12(s, s, pr[i][0], pr[i][1])

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
type_design = [11, 12, 11, 12, 11, 12, 11, 12, 11]

design45(data, pr_data, type_design)

turtle.hideturtle()
turtle.done()