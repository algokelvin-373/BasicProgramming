import turtle

def design8(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()

    space = 0
    while space <= side:
        radius = side - space
        if space == 0:
            turtle.begin_fill()
        turtle.forward(space)
        turtle.circle(radius, 90)
        turtle.forward(space)
        turtle.right(270)
        turtle.forward(space)
        turtle.circle(radius, 90)
        turtle.forward(space)
        turtle.right(-90)
        if space == 0:
            turtle.end_fill()
        space += 30

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

design8(200, 200)

turtle.hideturtle()
turtle.done()