import turtle

def design5(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    x_start = -x/2
    y_start = -y/2
    x_finish = -x
    y_finish = -y
    while x_start >= x_finish:
        s = abs(x_start + x_finish)
        turtle.penup()
        turtle.goto(x_start, y_start)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(s)
            turtle.left(90)
        x_start -= 5
        y_start -= 5

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

design5(200, 200)

turtle.hideturtle()
turtle.done()