import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(1)

side = 20
line_color1 = ['red', 'green', 'blue']
line_color2 = ['green', 'blue', 'red']
line_color3 = ['blue', 'red', 'green']
for i in range(40):
    colors = line_color1
    if i % 2 == 0:
        colors = line_color2
    elif i % 3 == 0:
        colors = line_color3
    turtle.penup()
    turtle.goto(-side / 2, -side / 2)
    turtle.pendown()
    for j in range(3):
        turtle.color(colors[j])
        turtle.forward(side)
        turtle.left(120)
    side += 10

turtle.hideturtle()
turtle.done()