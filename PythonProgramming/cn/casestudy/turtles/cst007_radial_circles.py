import turtle

def radial_circles(side, angle):
    count = 0
    while count <= 360:
        turtle.penup()
        turtle.pendown()
        turtle.circle(side)
        turtle.left(angle)
        count += angle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(0)
turtle.speed(0)

radial_circles(100,  5)

turtle.hideturtle()
turtle.done()