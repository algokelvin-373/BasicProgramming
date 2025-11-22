import turtle

def design16(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    step = 10

    y_finish = -y
    for _ in range(int(side/step) + 1):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.goto(x, y_finish)
        turtle.left(step)
        y_finish += step

    x_finish = x
    for _ in range(int(side/step) + 1):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.goto(x_finish, y)
        turtle.left(step)
        x_finish -= step

    y_finish = y
    for _ in range(int(side / step) + 1):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.goto(-x, y_finish)
        turtle.left(step)
        y_finish -= step

    x_finish = -x
    for _ in range(int(side / step) + 1):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.goto(x_finish, -y)
        turtle.left(step)
        x_finish += step

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

design16(200, 200)

turtle.hideturtle()
turtle.done()