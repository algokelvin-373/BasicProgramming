import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(1)
turtle.speed(0)

angle = 5
for i in range(int(360 / angle)):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.forward(50)
    turtle.pendown()
    for _ in range(4):
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.circle(-50, steps=4)
        turtle.left(90)
    turtle.left(angle)

turtle.hideturtle()
turtle.done()