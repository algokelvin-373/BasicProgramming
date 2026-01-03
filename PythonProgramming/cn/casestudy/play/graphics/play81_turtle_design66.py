import turtle

def dgn_obj(r):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.forward(r)
    turtle.pendown()

    turtle.begin_fill()
    for _ in range(2):
        turtle.circle(r, -90)
        turtle.circle(-r, 90)
    turtle.end_fill()

def design66(r, angle):
    times = 1
    colors = ['aqua', 'blue']
    for _ in range(int(90 / angle) + 1):
        turtle.color(colors[_ % 2])
        dgn_obj(r)
        turtle.right(angle)
        times += 1


turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(2)
turtle.speed(0)

design66(200, 5)

turtle.hideturtle()
turtle.done()