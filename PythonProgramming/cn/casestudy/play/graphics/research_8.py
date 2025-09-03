import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(1)
turtle.speed(0)

n = 20
x_start = 0
y_start = 0
side = 200
angle = 360 / n

x = []
y = []

turtle.goto(x_start, y_start)
for _ in range(n):
    turtle.forward(side)
    print(f'x: {turtle.xcor()}')
    x.append(turtle.xcor())
    y.append(turtle.ycor())
    print(f'y: {turtle.ycor()}')
    turtle.begin_fill()
    turtle.circle(2)
    turtle.end_fill()
    turtle.goto(x_start, y_start)
    turtle.left(angle)

for i in range(len(x)):
    xs = x[i]
    ys = y[i]
    for j in range(len(x)):
        turtle.goto(xs, ys)
        xf = x[j]
        yf = y[j]
        turtle.goto(xf, yf)



# turtle.goto(x_start, y_start)
# turtle.forward(side)
# turtle.begin_fill()
# turtle.circle(2)
# turtle.end_fill()
#
# turtle.goto(x_start, y_start)
# turtle.left(180)
# turtle.forward(side)
# turtle.begin_fill()
# turtle.circle(2)
# turtle.end_fill()


turtle.hideturtle()
turtle.done()