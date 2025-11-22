import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(1)

side = 20
line_color1 = ['red', 'green', 'blue']
line_color2 = ['green', 'blue', 'red']
line_color3 = ['blue', 'red', 'green']

for i in range(2):
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

side = 20
x_now = -side / 2
y_now = -side / 2
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

turtle.left(60)

turtle.forward(side)
turtle.left(120)
turtle.forward(side)
turtle.left(120)
turtle.forward(side)
turtle.left(120)

side = 40
y = turtle.ycor()
x_now = turtle.xcor()
y_now = y - 10
turtle.penup()
turtle.goto(x_now, y_now)
turtle.pendown()

# turtle.left(120)
turtle.forward(side)
turtle.left(120)
turtle.forward(side)
turtle.left(120)
turtle.forward(side)
turtle.left(120)

# turtle.forward(side)
# turtle.left(120)
# turtle.forward(side)
# turtle.left(120)
#
# side = 40
# turtle.penup()
# turtle.goto(20, 20)
# turtle.pendown()
#
# turtle.forward(side)


# for i in range(5):
#     colors = line_color1
#     if i % 2 == 0:
#         colors = line_color2
#     elif i % 3 == 0:
#         colors = line_color3
#     turtle.penup()
#     turtle.goto(-side / 2, side / 2)
#     turtle.pendown()
#
#     turtle.setheading(240)
#
#     for j in range(3):
#         turtle.color(colors[j])
#         turtle.forward(side)
#         turtle.left(120)
#     side += 10

turtle.hideturtle()
turtle.done()