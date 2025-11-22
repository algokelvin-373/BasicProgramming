import turtle

def radial_circles(side, angle):
    turtle.penup()
    turtle.goto(0, 220)
    turtle.write(
        f'n = {angle} | side = {side}',
        align='center',
        font=('Arial', 16, 'bold')
    )
    count = 0
    turtle.goto(0, 0)
    turtle.pendown()
    while count <= 360:
        turtle.penup()
        turtle.pendown()
        turtle.circle(side)
        turtle.left(angle)
        count += angle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(0)
turtle.speed(0)

n = 10
side = 100
while n >= 4:
    radial_circles(100,  n)
    turtle.clear()
    n -= 2

n = 10
side = 100
while side >= 10:
    radial_circles(side,  n)
    turtle.clear()
    side -= 10

turtle.hideturtle()
turtle.done()