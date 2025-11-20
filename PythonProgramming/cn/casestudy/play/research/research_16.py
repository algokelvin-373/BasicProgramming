import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(1)

turtle.left(90)

radius = 50
side = 0
for _ in range(5):
    turtle.circle(radius, 90)
    side += 10
    turtle.penup()
    turtle.goto(side, 0)
    turtle.pendown()
    turtle.left(-90)
    radius += 10


turtle.hideturtle()
turtle.done()