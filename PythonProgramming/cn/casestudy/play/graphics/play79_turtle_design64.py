import turtle

def design64(r, angle):
    for _ in range(int(180/angle)):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.circle(r, 90)
        turtle.circle(-r/2, -90)
        turtle.left(10)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(2)
turtle.speed(0)

design64(150, 5)

turtle.hideturtle()
turtle.done()