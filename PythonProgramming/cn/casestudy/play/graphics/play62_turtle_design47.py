import turtle

def design16(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    step = 10

    y_finish = yr + -y
    for _ in range(int(side/step) + 1):
        turtle.penup()
        turtle.goto(xr + 0, yr + 0)
        turtle.pendown()
        turtle.goto(xr + x, y_finish)
        turtle.left(step)
        y_finish += step

    x_finish = xr + x
    for _ in range(int(side/step) + 1):
        turtle.penup()
        turtle.goto(xr + 0, yr + 0)
        turtle.pendown()
        turtle.goto(x_finish, yr + y)
        turtle.left(step)
        x_finish -= step

    y_finish = yr + y
    for _ in range(int(side / step) + 1):
        turtle.penup()
        turtle.goto(xr + 0, yr + 0)
        turtle.pendown()
        turtle.goto(xr + -x, y_finish)
        turtle.left(step)
        y_finish -= step

    x_finish = xr + -x
    for _ in range(int(side / step) + 1):
        turtle.penup()
        turtle.goto(xr + 0, yr + 0)
        turtle.pendown()
        turtle.goto(x_finish, yr + -y)
        turtle.left(step)
        x_finish += step

def design17(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    step = 10

    x_finish = xr + -x
    for _ in range(int(side/step) + 1):
        turtle.penup()
        turtle.goto(xr + -x, yr + -y)
        turtle.pendown()
        turtle.goto(x_finish, yr + y)
        turtle.left(step)
        x_finish += step

    y_finish = yr + y
    for _ in range(int(side / step) + 1):
        turtle.penup()
        turtle.goto(xr + -x, yr + -y)
        turtle.pendown()
        turtle.goto(xr + x, y_finish)
        turtle.left(step)
        y_finish -= step

def design18(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    step = 10

    x_finish = xr + x
    for _ in range(int(side/step) + 1):
        turtle.penup()
        turtle.goto(xr + x, yr + -y)
        turtle.pendown()
        turtle.goto(x_finish, yr + y)
        turtle.left(step)
        x_finish -= step

    y_finish = yr + y
    for _ in range(int(side / step) + 1):
        turtle.penup()
        turtle.goto(xr + x, yr + -y)
        turtle.pendown()
        turtle.goto(xr + -x, y_finish)
        turtle.left(step)
        y_finish -= step

def design19(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    step = 10

    x_finish = xr + x
    for _ in range(int(side/step) + 1):
        turtle.penup()
        turtle.goto(xr + x, yr + y)
        turtle.pendown()
        turtle.goto(x_finish, yr + -y)
        turtle.left(step)
        x_finish -= step

    y_finish = yr + -y
    for _ in range(int(side / step) + 1):
        turtle.penup()
        turtle.goto(xr + x, yr + y)
        turtle.pendown()
        turtle.goto(xr + -x, y_finish)
        turtle.left(step)
        y_finish += step

def design20(x, y, xr, yr):
    side = x + y

    turtle.penup()
    turtle.goto(xr + -x, yr + -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    step = 10

    x_finish = xr + -x
    for _ in range(int(side/step) + 1):
        turtle.penup()
        turtle.goto(xr + -x, yr + y)
        turtle.pendown()
        turtle.goto(x_finish, yr + -y)
        turtle.left(step)
        x_finish += step

    y_finish = yr + -y
    for _ in range(int(side / step) + 1):
        turtle.penup()
        turtle.goto(xr + -x, yr + y)
        turtle.pendown()
        turtle.goto(xr + x, y_finish)
        turtle.left(step)
        y_finish += step

def design46(s, pr, typ):
    for i in range(len(pr)):
        if typ[i] == 16:
            design16(s, s, pr[i][0], pr[i][1])
            turtle.setheading(0)
        elif typ[i] == 17:
            design17(s, s, pr[i][0], pr[i][1])
            turtle.setheading(0)
        elif typ[i] == 18:
            design18(s, s, pr[i][0], pr[i][1])
            turtle.setheading(0)
        elif typ[i] == 19:
            design19(s, s, pr[i][0], pr[i][1])
            turtle.setheading(0)
        elif typ[i] == 20:
            design20(s, s, pr[i][0], pr[i][1])
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
type_design = [18, 16, 17, 16, 16, 16, 19, 16, 20]

design46(data, pr_data, type_design)

turtle.hideturtle()
turtle.done()