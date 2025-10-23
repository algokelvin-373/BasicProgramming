import turtle


turtle.setup(width=500, height=500)
turtle.bgcolor('white')
turtle.color('salmon')
turtle.pensize(1)

r = 200
angle = 90

turtle.penup()
turtle.forward(r)
turtle.pendown()
for _ in range(2):
    turtle.circle(r, -angle)
    turtle.circle(-r, angle)

turtle.hideturtle()
turtle.done()