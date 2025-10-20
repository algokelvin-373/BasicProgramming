import turtle


def draw_square(side, count, step):
    for i in range(count):
        turtle.penup()
        turtle.goto(-side/2, -side/2)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)
        side += 2 * step


turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(0)

draw_square(40, 25, 5)

turtle.hideturtle()
turtle.done()