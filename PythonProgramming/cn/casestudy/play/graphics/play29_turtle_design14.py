import turtle

def design11(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.penup()
    turtle.goto(200,200)
    turtle.pendown()

    turtle.right(90)

    radius = 0
    x_side = x
    y_side = y
    while x_side >= -x:
        turtle.circle(radius, 90)
        x_side -= 10
        turtle.penup()
        turtle.goto(x_side, y_side)
        turtle.pendown()
        turtle.left(-90)
        radius += 10
    x_side += 10
    radius -= 10
    while y_side >= -y:
        turtle.penup()
        turtle.goto(x_side, y_side)
        turtle.pendown()
        turtle.circle(radius, 90)
        y_side -= 30
        turtle.left(-90)
        radius -= 30

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

design11(200, 200)

turtle.hideturtle()
turtle.done()