import turtle

def design11(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    x_start = -x
    y_start = y
    x_finish = x
    y_finish = -y

    x1  = x_start
    while x1 < x_finish:
        turtle.penup()
        turtle.goto(x1, y_start)
        turtle.pendown()
        turtle.goto(x1, y_finish)
        x1 += 5

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

design11(200, 200)

turtle.hideturtle()
turtle.done()