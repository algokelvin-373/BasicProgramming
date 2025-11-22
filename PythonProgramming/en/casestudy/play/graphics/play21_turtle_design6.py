import turtle

def design6(x, y):
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
    turtle.penup()
    turtle.goto(x_start, y_start)
    turtle.pendown()

    x1 = x_start
    y1 = y_start
    x2 = x_start
    y2 = y_start
    while y1 >= y_finish:
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)
        y1 -= 10
        x2 += 10

    turtle.penup()
    turtle.goto(-100, -100)
    turtle.pendown()
    turtle.color('salmon', 'black')
    turtle.begin_fill()
    turtle.goto(100, 100)
    turtle.goto(-100, 100)
    turtle.goto(-100, -100)
    turtle.end_fill()
    turtle.color('salmon')
    turtle.begin_fill()
    turtle.goto(100, 100)
    turtle.goto(100, -100)
    turtle.goto(-100, -100)
    turtle.end_fill()

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

design6(200, 200)

turtle.hideturtle()
turtle.done()