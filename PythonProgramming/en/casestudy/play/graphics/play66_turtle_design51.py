import turtle

def design51(r):
    angle = 90
    side = 10
    for _ in range(int(90/side)):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.forward(r)
        turtle.pendown()
        for _ in range(2):
            turtle.circle(r, -angle)
            turtle.circle(-r, angle)
        turtle.right(side)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(1)
turtle.speed(0)

design51(200)

turtle.hideturtle()
turtle.done()