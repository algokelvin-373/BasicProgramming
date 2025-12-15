import turtle

colors = ['magenta', 'lightblue', 'yellow'
          ,'orange', 'lightgreen', 'pink']

def obj(r):
    for _ in range(4):
        turtle.forward(r)
        turtle.left(90)
        turtle.forward(r)
        turtle.circle(r, -90)
        turtle.left(90)

def design72(r, angle):
    for i in range(int(90/angle)):
        r1 = r/2
        turtle.color(colors[i % 6])
        for _ in range(10):
            obj(r1)
            r1 += 10
        turtle.left(angle)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(1)
turtle.speed(0)

design72(150, 10)

turtle.hideturtle()
turtle.done()