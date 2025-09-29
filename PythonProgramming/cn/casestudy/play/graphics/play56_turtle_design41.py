import turtle


def design1(x, y, xr = 0, yr = 0):
    side = x + y
    # square center
    turtle.penup()
    turtle.goto(xr + -x/2, yr + -y/2)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(x)
        turtle.left(90)
    turtle.end_fill()

    # side 1
    x1 = xr + -x
    y1 = yr + y
    while x1 < (xr + -int(x/2)):
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(int(0.75 * side))
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(int(0.75 * side))
        turtle.right(90)
        x1 += 10
    while y1 > (yr + int(y/2)):
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.forward(int(0.75 * side))
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(int(0.75 * side))
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        y1 -= 10

    turtle.right(180)

    # Side 2
    x1 = xr + x
    y1 = yr + -y

    while x1 > (xr + int(x/2)):
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(int(0.75 * side))
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(int(0.75 * side))
        turtle.right(90)
        x1 -= 10
    while y1 < (yr + -int(y/2)):
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.forward(int(0.75 * side))
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(int(0.75 * side))
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        y1 += 10

    turtle.setheading(0)

def design41(s, pr):
    for i in range(len(pr)):
        design1(s, s, pr[i][0], pr[i][1])

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

design41(data, pr_data)

turtle.hideturtle()
turtle.done()