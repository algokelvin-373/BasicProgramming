import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(1)
turtle.speed(0)

s = 500
j = 0
colors = ['red', 'green', 'blue']
for i in range(50):
    if j == len(colors):
        j = 0
    color = colors[j]
    turtle.penup()
    turtle.goto(-s/2, -s/2)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(s)
        turtle.left(90)
    turtle.end_fill()
    s -= 10
    j += 1

turtle.hideturtle()
turtle.done()