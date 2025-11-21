import turtle
import time

turtle.setup(width=500, height=500)
turtle.bgcolor('lightblue')
turtle.tracer(0)    # Just focus animation

turtle.shape('circle')
turtle.color('red')
turtle.shapesize(stretch_wid=3, stretch_len=3)
turtle.penup()
turtle.goto(-300, 25)

velocity = 2
turn = 1    # -1: left  1:right

while True:
    turtle.update()
    time.sleep(0.01)
    x = turtle.xcor()
    turtle.setx(x + velocity * turn)
    if x > 300:
        turn = -1
    elif x < -300:
        turn = 1
