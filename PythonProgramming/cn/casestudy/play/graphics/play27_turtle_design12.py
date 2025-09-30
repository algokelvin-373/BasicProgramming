import turtle

def design12(x, y):
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

    y1 = y_start
    while y1 > y_finish:
        turtle.penup()
        turtle.goto(x_start, y1)
        turtle.pendown()
        turtle.goto(x_finish, y1)
        y1 -= 5

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

design12(200, 200)

turtle.hideturtle()
turtle.done()