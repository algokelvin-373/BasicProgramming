import turtle

def bezier(t, p0, p1, p2):
    x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
    y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
    return x, y

def curva(p0, pc, p1):
    for i in range(101):
        t_bezier = i / 100
        x, y = bezier(t_bezier, p0, pc, p1)
        if i == 0:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
        else:
            turtle.goto(x, y)

def draw_top_curva(p0, p1, pc, side, step, position):
    x_start = p0[0]
    y_start = p0[1]
    x_finish = p1[0]
    y_finish = p1[1]
    for _ in range(int(side / step)):
        t0 = (x_start, y_start)
        t1 = (x_finish, y_finish)
        curva(t0, pc, t1)
        if position == "+":
            y_start += step
            x_finish -= step
        elif position == "-":
            x_start += step
            y_finish -= step

def draw_curva(xt, yt, p0, p1, side, position):
    pc = (xt, yt)
    step = 10

    draw_top_curva(p0, p1, pc, side, step, position)

    for _ in range(int(side / step)):
        curva(p0, pc, p1)
        if xt < 0:
            xt += 10
        else:
            xt -= 10
        if yt < 0:
            yt += 10
        else:
            yt -= 10
        pc = (xt, yt)

def design29(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    p0 = (-x, -y)
    p1 = (x, y)

    side = x
    draw_curva(-x, y, p0, p1, side, "+")
    draw_curva(x, -y, p0, p1, side, "-")

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(1)
turtle.speed(0)

design29(200, 200)

turtle.hideturtle()
turtle.done()