import turtle


def design63(r, angle):
    alfa = 180
    for i in range(int(180/angle)):
        if i % 2 == 0:
            alfa = 180
            turtle.circle(r, alfa)
        else:
            alfa = -90
            turtle.circle(r, alfa)
            turtle.penup()
            turtle.goto(0, 0)
            turtle.pendown()
        turtle.left(angle)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(2)
turtle.speed(0)

design63(100, 5)

turtle.hideturtle()
turtle.done()