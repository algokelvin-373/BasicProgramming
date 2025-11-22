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

def step_discrete(point, step=10):
    x, y = point

    if x > 0:
        x = max(x - step, 0)
    elif x < 0:
        x = min(x + step, 0)

    if y > 0:
        y = max(y - step, 0)
    elif y < 0:
        y = min(y + step, 0)

    return x, y

def step_discrete2(point, step=10, full=200):
    x, y = point

    x_step = 0
    if abs(x) == full // 2:
        x_step = step / 2
    else:
        x_step = step

    y_step = 0
    if abs(y) == full // 2:
        y_step = step / 2
    else:
        y_step = step

    if x > 0:
        x = max(x - x_step, 0)
    elif x < 0:
        x = min(x + x_step, 0)

    if y > 0:
        y = max(y - y_step, 0)
    elif y < 0:
        y = min(y + y_step, 0)

    return x, y

def design50(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.goto(x, y)
    turtle.goto(x, -y)
    turtle.goto(-x, y)
    turtle.goto(-x, 0)
    turtle.goto(x, 0)
    turtle.goto(x, y)
    turtle.goto(0, y)
    turtle.goto(0, -y)

    ps = [
        (-x, -y),
        (0, -y),
        (x, -y),
        (x, 0),
        (x, y),
        (0, y),
        (-x, y),
        (-x, 0)
    ]
    pf = [
        (0, -y),
        (x, -y),
        (x, 0),
        (x, y),
        (0, y),
        (-x, y),
        (-x, 0),
        (-x, -y)
    ]

    pt = [
        (-x / 2, -y),
        (x / 2, -y),
        (x, -y / 2),
        (x, y / 2),
        (x / 2, y),
        (-x / 2, y),
        (-x, y / 2),
        (-x, -y / 2),
    ]

    step = 10
    for _ in range(int(x/step)):
        for i in range(len(ps)):
            curva(ps[i], pt[i], pf[i])
        for i in range(len(ps)):
            pt[i] = step_discrete2(pt[i], full=x)

    pc = (0,0)
    for _ in range(int(x/step)):
        for i in range(len(ps)):
            curva(ps[i], pc, pf[i])
        for i in range(len(ps)):
            ps[i] = step_discrete(ps[i])
            pf[i] = step_discrete(pf[i])

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(1)
turtle.speed(0)

design50(200, 200)

turtle.hideturtle()
turtle.done()