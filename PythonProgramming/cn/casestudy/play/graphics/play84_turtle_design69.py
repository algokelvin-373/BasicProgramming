import turtle

colors = ['magenta', 'lightblue', 'yellow'
          ,'orange', 'lightgreen', 'pink']

def obj(r):
    turtle.circle(r, 180)
    turtle.circle(r / 2, 180)
    turtle.circle(-r / 2, 180)

def design69(r, angle):
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

design69(50, 10)

turtle.hideturtle()
turtle.done()