import turtle

def design56(r, angle):
    for _ in range(int(90/angle)):
        for _ in range(4):
            turtle.forward(r)
            turtle.left(90)
            turtle.forward(r)
            turtle.circle(r, -90)
            turtle.left(90)
        turtle.left(angle)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(1)
turtle.speed(0)

design56(150, 10)

turtle.hideturtle()
turtle.done()