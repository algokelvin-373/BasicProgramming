import turtle

colors = ['red', 'aqua', 'yellow'
          ,'orange', 'green', 'magenta']

def obj(r):
    for _ in range(2):
        turtle.circle(r, 90)
        turtle.left(90)

def design71(r, angle):
    for i in range(int(360/angle)):
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

design71(150, 10)

turtle.hideturtle()
turtle.done()