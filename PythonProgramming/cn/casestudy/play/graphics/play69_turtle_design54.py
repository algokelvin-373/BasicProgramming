import turtle

def design54(r, angle):
    for _ in range(int(360/angle)):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.circle(r/2, 180)
        turtle.left(180)
        turtle.circle(r/2, 180)
        turtle.left(180)
        turtle.left(angle)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(1)
turtle.speed(0)

design54(100, 10)

turtle.hideturtle()
turtle.done()