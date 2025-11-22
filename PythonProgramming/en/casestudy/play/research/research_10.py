import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(1)
turtle.speed(0)

side = 100
for i in range(50):
    turtle.penup()
    turtle.circle(i * 2, 120)
    turtle.pendown()
    turtle.circle(side)

turtle.hideturtle()
turtle.done()