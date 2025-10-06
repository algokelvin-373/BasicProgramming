import turtle

def design54(r, angle):
    step = int(360/angle)
    for i in range(step):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        if i >= step/2:
            turtle.circle(r / 2, 180)
            turtle.left(180)
            turtle.circle(r / 2, -180)
            turtle.left(180)
        else:
            turtle.circle(r / 2, -180)
            turtle.left(180)
            turtle.circle(r / 2, 180)
            turtle.left(180)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        if i >= step / 2:
            turtle.circle(-r / 2, -180)
            turtle.left(180)
            turtle.circle(-r / 2, 180)
            turtle.left(180)
        else:
            turtle.circle(-r / 2, 180)
            turtle.left(180)
            turtle.circle(-r / 2, -180)
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