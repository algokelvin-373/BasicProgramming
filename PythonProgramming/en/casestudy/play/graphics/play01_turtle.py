import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(1)

r = 15
for i in range(30):
    turtle.up()
    turtle.goto(0, -r)
    turtle.down()
    if i % 2 == 0:
        turtle.circle(r + 10)
    else:
        for _ in range(4):
            turtle.forward(r + 30)
            turtle.left(90)
    r += 5

turtle.hideturtle()
turtle.done()