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

def draw_curva(xt, yt, p0, p1, side):
    pc = (xt, yt)
    step = 10

    for _ in range(int(side / step)):
        curva(p0, pc, p1)
        if yt > 0:
            yt -= step
        else:
            yt += step
        pc = (xt, yt)

def design30(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    p0 = (-x, 0)
    p1 = (x, 0)

    side = x
    draw_curva(0, y, p0, p1, side)
    draw_curva(0, -y, p0, p1, side)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(1)
turtle.speed(0)

design30(200, 200)

turtle.hideturtle()
turtle.done()