import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(2)

s = 10
for i in range(50):
    if i % 2 == 0:
        turtle.color('red')
    else:
        turtle.color('blue')
    turtle.penup()
    turtle.goto(-s/2, -s/2)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(s)
        turtle.left(90)
    s += 2 * 5

turtle.hideturtle()
turtle.done()