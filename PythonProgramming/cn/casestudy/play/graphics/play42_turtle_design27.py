import turtle

def design27(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.penup()
    turtle.goto(0, -y)
    turtle.pendown()
    turtle.circle(side/2, steps=4)

    x_finish = -x
    y_finish = 0
    step = 5
    for _ in range(int(x/step)):
        turtle.penup()
        turtle.goto(-x, y)
        turtle.pendown()
        turtle.goto(x_finish, y_finish)
        x_finish += step
        y_finish += step

    x_finish = x
    y_finish = 0
    step = 5
    for _ in range(int(x / step)):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x_finish, y_finish)
        x_finish -= step
        y_finish += step

    x_finish = -x
    y_finish = 0
    step = 5
    for _ in range(int(x / step)):
        turtle.penup()
        turtle.goto(-x, -y)
        turtle.pendown()
        turtle.goto(x_finish, y_finish)
        x_finish += step
        y_finish -= step

    x_finish = x
    y_finish = 0
    step = 5
    for _ in range(int(x / step)):
        turtle.penup()
        turtle.goto(x, -y)
        turtle.pendown()
        turtle.goto(x_finish, y_finish)
        x_finish -= step
        y_finish -= step

    radius = 0
    y_side = 0
    step = 5
    for _ in range(int(y/step)):
        turtle.penup()
        turtle.goto(0, y_side)
        turtle.pendown()
        turtle.circle(radius)
        radius += step
        y_side -= step


turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(1)
turtle.speed(0)

design27(200, 200)

turtle.hideturtle()
turtle.done()