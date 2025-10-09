import turtle


def design61(r, angle):
    for _ in range(int(360/angle)):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        radius = 0
        counts = int(r/angle)
        for i in range(counts):
            if i >= counts/2:
                radius -= 2
            else:
                radius += 2
            turtle.circle(radius)
            turtle.penup()
            turtle.forward(angle)
            turtle.pendown()
        turtle.left(angle)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(2)
turtle.speed(0)

design61(200, 10)

turtle.hideturtle()
turtle.done()