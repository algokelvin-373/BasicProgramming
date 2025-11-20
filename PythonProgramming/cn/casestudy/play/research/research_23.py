import turtle

def bezier(t, p0, p1, p2):
    x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
    y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
    return x, y

def curva(P0, P1, P2):
    for i in range(101):
        t_bezier = i / 100
        x, y = bezier(t_bezier, P0, P1, P2)
        if i == 0:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
        else:
            turtle.goto(x, y)

turtle.setup(width=500, height=500)
turtle.bgcolor('white')
turtle.color('salmon')
turtle.pensize(1)
turtle.speed(0)

P0 = (-200, -200)
P2 = (200, 200)
P1 = (-200, 200)

turtle.penup()

turtle.goto(P0)
turtle.dot(8, "green")
turtle.write(" P0")

turtle.goto(P1)
turtle.dot(8, "gray")
turtle.write(" P1 (kontrol)")

turtle.goto(P2)
turtle.dot(8, "red")
turtle.write(" P2")

turtle.pendown()

turtle.goto(P0)
turtle.goto(P1)
turtle.goto(P2)

turtle.color("blue")
turtle.pensize(2)

xt = -200
yt = 200
for _ in range(10):
    curva(P0, P1, P2)
    xt += 10
    yt -= 10
    P1 = (xt, yt)

turtle.hideturtle()
turtle.done()