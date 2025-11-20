import math
import turtle

# Parameter
CENTER = (0, 0)
RADIUS = 100

def on_click(x, y):
    distance = math.sqrt((x - CENTER[0]) ** 2 + (y - CENTER[1]) ** 2)

    text_turtle.clear()

    if distance <= RADIUS:
        message = "Anda klik di dalam lingkaran"
        text_turtle.color("lime")
    else:
        message = "Anda klik di luar lingkaran"
        text_turtle.color("red")

    text_turtle.goto(0, -150)
    text_turtle.write(
        message,
        align="center",
        font=("Arial", 16, "bold")
    )

turtle.setup(width=500, height=700)
turtle.bgcolor('black')
turtle.color('lightblue', 'salmon')
turtle.pensize(3)
turtle.speed(1)

turtle.penup()
turtle.goto(0, 250)
turtle.write(
    f"‘Click’操作\n"
    f"Click Action\n"
    f"Aksi Click",
    align="center",
    font=("Arial", 16, "bold")
)

turtle.goto(CENTER[0], CENTER[1] - RADIUS)
turtle.pendown()
turtle.begin_fill()
turtle.circle(RADIUS)
turtle.end_fill()

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color('yellow')

turtle.onscreenclick(on_click)

turtle.hideturtle()
turtle.done()