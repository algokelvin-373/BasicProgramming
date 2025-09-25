import turtle

def design23(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    x_start = -x
    y_start = -y
    x_finish = x
    y_finish = -y
    x_side = 0
    y_side = 0
    for _ in range(int(y/10)):
        turtle.goto(x_start, y_start)
        turtle.goto(x_side, y_side)
        turtle.goto(x_finish, y_finish)
        y_side -= 10

    x_start = -x
    y_start = y
    x_finish = x
    y_finish = y
    x_side = 0
    y_side = 0
    for _ in range(int(y / 10)):
        turtle.goto(x_start, y_start)
        turtle.goto(x_side, y_side)
        turtle.goto(x_finish, y_finish)
        y_side += 10

    x_start = -x
    y_start = y
    x_finish = -x
    y_finish = -y
    x_side = 0
    y_side = 0
    for _ in range(int(x / 10)):
        turtle.goto(x_start, y_start)
        turtle.goto(x_side, y_side)
        turtle.goto(x_finish, y_finish)
        x_side -= 10

    x_start = x
    y_start = y
    x_finish = x
    y_finish = -y
    x_side = 0
    y_side = 0
    for _ in range(int(x / 10)):
        turtle.goto(x_start, y_start)
        turtle.goto(x_side, y_side)
        turtle.goto(x_finish, y_finish)
        x_side += 10

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(10)

design23(200, 200)

turtle.hideturtle()
turtle.done()