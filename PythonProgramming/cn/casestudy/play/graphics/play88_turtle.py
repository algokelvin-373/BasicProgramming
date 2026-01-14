import turtle
from colorsys import hsv_to_rgb

def draw_area(r):
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.circle(r)

def get_coordinates(r, angle):
    t_c = []
    for _ in range(int(360/angle)):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.forward(r)
        turtle.pendown()
        xc = turtle.xcor()
        yc = turtle.ycor()
        t_c.append((xc, yc))
        turtle.left(angle)
    return t_c

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('white')
turtle.pensize(1)
turtle.speed(0)

r1 = 200
yt = -100
h = 0
alpha = 2
turtle.tracer(0, 0)
draw_area(r1)
turtle.tracer(1)
tc = get_coordinates(r1, alpha)
for i in range(5):
    for t in tc:
        turtle.color(hsv_to_rgb(h, 1,1))
        turtle.penup()
        turtle.goto(0, yt)
        turtle.pendown()
        turtle.goto(t[0], t[1])
        h += 0.005

turtle.hideturtle()
turtle.done()