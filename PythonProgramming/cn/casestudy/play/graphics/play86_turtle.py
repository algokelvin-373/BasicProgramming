import turtle

colors = ['lightgreen', 'lightblue', 'orange']

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(1)
turtle.speed(0)

n = 5
angle = 360/n + 45
count_colors = len(colors)
for i in range(360):
    turtle.color(colors[i % count_colors])
    turtle.forward(i)
    turtle.right(angle)

turtle.hideturtle()
turtle.done()