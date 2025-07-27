import turtle

turtle.color('black')
turtle.pensize(0)

r = 20
for i in range (9):
    turtle.up()
    turtle.goto(0, -r)
    turtle.down()
    turtle.circle(r + 20)
    r += 20