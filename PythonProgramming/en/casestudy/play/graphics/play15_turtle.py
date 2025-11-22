import turtle

def draw(side):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(side, 90)
    turtle.right(270)
    turtle.circle(side, 90)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(10)

for _ in range(4):
    draw(200)
    turtle.left(180)

turtle.hideturtle()
turtle.done()