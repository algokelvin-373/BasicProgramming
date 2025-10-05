import turtle

def design52(r):
    step = 10
    for _ in range(int(90/step)):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        for _ in range(4):
            turtle.circle(r/2, 90)
            turtle.right(90)
            turtle.circle(-r/2, -90)
        turtle.right(step)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(1)
turtle.speed(0)

design52(200)

turtle.hideturtle()
turtle.done()