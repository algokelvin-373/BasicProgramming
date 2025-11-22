import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(1)
turtle.speed(0)

for i in range(60):
    turtle.circle(i * 2)
    turtle.right(10)

turtle.hideturtle()
turtle.done()