import turtle

def circle_design(n, side):
    if n > 6:
        turtle.speed(0)
    else:
        turtle.speed(10)
    turtle.penup()
    turtle.goto(0, 225)
    turtle.write(f"n = {n}", align="center", font=("Arial", 16, "bold"))

    x_start = 0
    y_start = 0
    angle = 360 / n

    x = []
    y = []
    turtle.goto(x_start, y_start)
    turtle.pendown()
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

    turtle.clear()

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(1)

for i in range(20):
    if i < 2:
        continue
    circle_design(i, 200)

turtle.hideturtle()
turtle.done()