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

def design32(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    step = 20
    x1, x2, x3 = -x, 0, x
    xc = x/2
    yc = y
    for _ in range(int(side/step)):
        p0 = (x1, yc)
        p1 = (x2, yc)
        p2 = (x3, yc)
        pc1 = (-xc, yc - step)
        pc2 = (xc, yc - step)
        curva(p0, pc1, p1)
        curva(p1, pc2, p2)
        yc -= step

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(1)
turtle.speed(10)

design32(200, 200)

turtle.hideturtle()
turtle.done()