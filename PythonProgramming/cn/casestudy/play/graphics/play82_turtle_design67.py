import turtle

colors = ['red', 'blue', 'green', 'magenta']

def design67(r):
    for i in range(150):
        turtle.pencolor(colors[i % 4])
        turtle.rt(i)
        turtle.circle(r, i)
        turtle.fd(i)
        turtle.rt(90)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(1)
turtle.speed(0)

design67(100)

turtle.hideturtle()
turtle.done()