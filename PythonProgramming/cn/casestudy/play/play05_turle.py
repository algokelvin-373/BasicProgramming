import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(1)
turtle.speed(0)

r = 200
colors = ['red', 'white']
for i in range(20):
    color = colors[i % 2]
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    r -= 10

turtle.hideturtle()
turtle.done()