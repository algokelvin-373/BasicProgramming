import turtle


def design62(r, angle):
    turtle.penup()
    turtle.goto(-r/2, -r/2)
    turtle.pendown()

    alfa = -90
    for _ in range(int(360/angle)):
        if alfa == -90:
            alfa = 90
        else:
            alfa  = -90
        turtle.circle(r, alfa)
        turtle.left(angle)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(2)
turtle.speed(0)

design62(300, 5)

turtle.hideturtle()
turtle.done()