import turtle

def design53(r, step):
    for _ in range(int(360/step)):
        turtle.circle(r, 180)
        turtle.circle(r / 2, 180)
        turtle.circle(-r / 2, 180)
        turtle.left(step)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(1)
turtle.speed(0)

design53(100, 5)

turtle.hideturtle()
turtle.done()