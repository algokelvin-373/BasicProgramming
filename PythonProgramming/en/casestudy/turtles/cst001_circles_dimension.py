import turtle

def draw_circle(r):
    s = r
    for i in range(10):
        turtle.up()
        turtle.goto(0, -r)
        turtle.down()
        turtle.circle(r + s)
        r += s


turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(0)

draw_circle(20)

turtle.hideturtle()
turtle.done()