import turtle

colors = ['blue', 'yellow', 'green', 'red']

def create_object(x):
    turtle.right(30)
    turtle.forward(x)
    turtle.left(60)
    turtle.forward(x)
    turtle.left(120)
    turtle.forward(x)
    turtle.left(60)
    turtle.forward(x)
    turtle.left(150)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.pensize(1)
turtle.speed(0)

alpha = 30
times = 360 / alpha
for _ in range(int(times)):
    s = 10
    for i in range(12):
        turtle.color(colors[i % 4])
        create_object(s)
        s += 10
    turtle.right(alpha)

turtle.hideturtle()
turtle.done()