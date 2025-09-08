import turtle

def radial_rectangle_dimension(side, dimension, count):
    for _ in range(dimension):
        s = side
        for _ in range(count):
            turtle.penup()
            turtle.pendown()
            for _ in range(3):
                turtle.forward(s)
                turtle.left(120)
            s += 5
        turtle.left(360/dimension)


turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(0)
turtle.speed(0)

radial_rectangle_dimension(20, 6, 30)

turtle.hideturtle()
turtle.done()