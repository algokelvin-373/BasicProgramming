import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(2)
turtle.speed(0)

n = 0
while n <= 360:
    turtle.goto(0,0)
    turtle.pendown()
    turtle.circle(150, 90, 3)
    turtle.penup()
    turtle.left(n + 10)
    n += 10


turtle.hideturtle()
turtle.done()