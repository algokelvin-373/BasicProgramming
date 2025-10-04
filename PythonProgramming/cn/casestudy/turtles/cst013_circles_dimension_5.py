import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(1)

side = 100
for _ in range(4):
    turtle.begin_fill()
    turtle.circle(side, 180)
    turtle.circle(side/2, 180)
    turtle.circle(-side/2, 180)
    turtle.end_fill()
    turtle.left(90)

turtle.hideturtle()
turtle.done()