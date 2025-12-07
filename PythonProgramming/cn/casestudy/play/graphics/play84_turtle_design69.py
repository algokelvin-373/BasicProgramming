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

def change_color(times):
    colors = ['aqua', 'blue']
    if times % 2 == 0:
        turtle.color(colors[0])
    else:
        turtle.color(colors[1])

def design69(r, angle):
    times = 1
    for _ in range(int(90 / angle) + 1):
        change_color(times)
        dgn_obj(r)
        turtle.right(angle)
        times += 1


turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(2)
turtle.speed(0)

design69(200, 5)

turtle.hideturtle()
turtle.done()