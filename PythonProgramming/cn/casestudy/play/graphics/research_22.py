import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(1)
turtle.speed(0)
turtle.colormode(255)

R1 = 0
R2 = 0
R3 = 0
side = 100
for i in range(720):
    if 0 <= i <= 240:
        R1 += 1
        turtle.color(R1, R1, 255)
    elif 241 <= i <= 480:
        R2 += 1
        turtle.color(R1, R2, R2)
    elif 481 <= i <= 720:
        R3 += 1
        turtle.color(R3, R2, R3)

    if i % 2 == 0:
        side += 1

    turtle.circle(side/4, steps=4)
    turtle.left(5)

turtle.hideturtle()
turtle.done()