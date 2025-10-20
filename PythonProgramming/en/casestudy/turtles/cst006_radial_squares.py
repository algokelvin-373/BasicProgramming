import turtle

def radial_squares(side, angle):
    count = 0
    while count <= 360:
        turtle.penup()
        turtle.pendown()
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)
        turtle.left(angle)
        count += angle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(0)
turtle.speed(0)

radial_squares(100,  1)

turtle.hideturtle()
turtle.done()