import turtle

def design2(s, xr, yr):
    for i in range(s):
        turtle.penup()
        turtle.goto(xr, yr)
        turtle.pendown()
        turtle.circle(i, 90)

    for i in range(s):
        turtle.penup()
        turtle.goto(xr, yr)
        turtle.pendown()
        turtle.circle(-i, 90)

    turtle.setheading(0)

def design6(x, y, xr, yr):
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

    turtle.penup()
    turtle.goto(xr + -x/2, yr + -y/2)
    turtle.pendown()
    turtle.color('salmon', 'black')
    turtle.begin_fill()
    turtle.goto(xr + x/2, yr + y/2)
    turtle.goto(xr + -x/2, yr + y/2)
    turtle.goto(xr + -x/2, yr + -y/2)
    turtle.end_fill()
    turtle.color('salmon')
    turtle.begin_fill()
    turtle.goto(xr + x/2, yr + y/2)
    turtle.goto(xr + x/2, yr + -y/2)
    turtle.goto(xr + -x/2, yr + -y/2)
    turtle.end_fill()

def design7(x, y, xr, yr):
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

    turtle.penup()
    turtle.goto(xr + x/2, yr + -y/2)
    turtle.pendown()
    turtle.color('salmon', 'black')
    turtle.begin_fill()
    turtle.goto(xr + x/2, yr + y/2)
    turtle.goto(xr + -x/2, yr + y/2)
    turtle.goto(xr + x/2, yr + -y/2)
    turtle.end_fill()
    turtle.color('salmon')
    turtle.begin_fill()
    turtle.goto(xr + -x/2, yr + -y/2)
    turtle.goto(xr + -x/2, yr + y/2)
    turtle.goto(xr + x/2, yr + -y/2)
    turtle.end_fill()

def design43(s, pr, typ):
    for i in range(len(pr)):
        if typ[i] == 2:
            design2(s, pr[i][0], pr[i][1])
        elif typ[i] == 6:
            design6(s, s, pr[i][0], pr[i][1])
        elif typ[i] == 7:
            design7(s, s, pr[i][0], pr[i][1])

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
type_design = [6, 2, 7, 7, 2, 6, 6, 2, 7]

design43(data, pr_data, type_design)

turtle.hideturtle()
turtle.done()