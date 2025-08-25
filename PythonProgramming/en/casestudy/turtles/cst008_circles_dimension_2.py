import turtle

def radial_circles_dimension(side, dimension):
    for _ in range(dimension):
        s = side
        for _ in range(20):
            turtle.penup()
            turtle.pendown()
            turtle.circle(s)
            s += 5
        turtle.left(360/dimension)


turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(0)
turtle.speed(0)

radial_circles_dimension(20, 6)

turtle.hideturtle()
turtle.done()