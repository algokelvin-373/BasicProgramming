import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(1)
turtle.speed(0)

for i in range(180):
    turtle.circle(i, i)

turtle.hideturtle()
turtle.done()