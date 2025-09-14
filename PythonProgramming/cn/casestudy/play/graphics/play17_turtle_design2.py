import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(2)
turtle.speed(0)

for i in range(180):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(i, 90)

for i in range(180):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(-i, 90)


turtle.hideturtle()
turtle.done()