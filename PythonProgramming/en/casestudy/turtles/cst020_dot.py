import turtle

turtle.setup(width=500, height=700)
turtle.bgcolor('black')
turtle.color('lightblue', 'salmon')
turtle.pensize(3)
turtle.speed(1)

turtle.penup()
turtle.goto(0, 150)
turtle.write(
    f"绘制点\n"
    f"Draw Dot\n"
    f"Menggambar Titik",
    align="center",
    font=("Arial", 16, "bold")
)

turtle.goto(0, 0)
turtle.dot(20, 'salmon')

turtle.hideturtle()
turtle.done()