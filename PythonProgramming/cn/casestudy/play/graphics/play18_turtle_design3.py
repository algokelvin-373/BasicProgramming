import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(0)

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

for _ in range(4):
    turtle.forward(400)
    turtle.left(90)

x_start = -200
y_start = 200
x_finish = 200
y_finish = -200
turtle.penup()
turtle.goto(x_start, y_start)
turtle.pendown()

x1 = x_start
y1 = y_start
x2 = x_start
y2 = y_start
while y1 >= y_finish:
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    y1 -= 10
    x2 += 10
y1 += 10
x2 -= 10
while x1 <= x_finish:
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    x1 += 10
    y2 -= 10

turtle.hideturtle()
turtle.done()