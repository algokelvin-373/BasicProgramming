import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(2)

r = 10
s = 5
for i in range(40):
    if i % 2 == 0:
        turtle.color('red')
    elif i % 2 and i % 3 == 0:
        turtle.color('blue')
    else:
        turtle.color('black')
    turtle.up()
    turtle.goto(0, -r)
    turtle.down()
    turtle.circle(r + s)
    r += s

turtle.hideturtle()
turtle.done()