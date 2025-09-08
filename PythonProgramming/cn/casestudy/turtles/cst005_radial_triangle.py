import turtle

def radial_triangles(side, angle):
    count = 0
    while count <= 360:
        turtle.penup()
        turtle.pendown()
        for _ in range(3):
            turtle.forward(side)
            turtle.left(120)
        turtle.left(angle)
        count += angle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(0)
turtle.speed(0)

radial_triangles(200,  5)

turtle.hideturtle()
turtle.done()