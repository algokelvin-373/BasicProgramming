import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(1)
turtle.speed(100)

colors = 'salmon'
for i in range(180):
    turtle.color(colors)
    turtle.circle(i * 2, 90)
    if i <= 90:
        turtle.circle(90)
    else:
        colors = 'lightblue'

turtle.hideturtle()
turtle.done()