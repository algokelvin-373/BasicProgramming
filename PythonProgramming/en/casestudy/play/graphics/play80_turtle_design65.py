import turtle

def draw_circle(r):
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.circle(r)

def design65(r, angle, xt):
    draw_circle(r)

    tc = []
    for _ in range(int(360/angle)):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.forward(r)
        turtle.pendown()
        xc = turtle.xcor()
        yc = turtle.ycor()
        tc.append((xc, yc))
        turtle.left(angle)

    for x in xt:
        for t in tc:
            turtle.penup()
            turtle.goto(x, 0)
            turtle.pendown()
            turtle.goto(t[0], t[1])

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(2)
turtle.speed(0)

design65(200, 5, [-100, 100])

turtle.hideturtle()
turtle.done()