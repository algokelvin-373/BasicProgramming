import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue', 'salmon')
turtle.pensize(3)
turtle.speed(1)

turtle.penup()
turtle.goto(0, 150)
turtle.write(
    f"用poly绘制角形\n"
    f"Draw Square with Poly\n"
    f"Menggambar Persegi dengan Poly",
    align="center",
    font=("Arial", 16, "bold")
)

side = 200
turtle.begin_fill()
turtle.begin_poly()
turtle.penup()
turtle.goto(-side/2, -side/2)
turtle.pendown()
for _ in range(4):
    turtle.forward(side)
    turtle.left(90)
turtle.end_poly()
turtle.end_fill()

turtle.hideturtle()
turtle.done()