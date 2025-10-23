import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(1)

x_finish = 100
y_finish = 0
for _  in range(11):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(x_finish, y_finish)
    turtle.left(10)
    y_finish += 10

for _  in range(11):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(x_finish, y_finish)
    turtle.left(10)
    x_finish -= 10

turtle.hideturtle()
turtle.done()