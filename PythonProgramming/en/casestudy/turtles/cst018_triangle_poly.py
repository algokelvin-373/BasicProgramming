import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue', 'salmon')
turtle.pensize(3)
turtle.speed(1)

# Implementation 'poly'
# 用poly画三角形
# Draw Triangle with "Poly"

turtle.penup()
turtle.goto(0, 150)
turtle.write(
    f"用poly画三角形\n"
    f"Draw Triangle with Poly\n"
    f"Menggambar Segitiga dengan Poly",
    align="center",
    font=("Arial", 16, "bold")
)

side = 200
turtle.begin_fill()
turtle.begin_poly()
turtle.penup()
turtle.goto(-side/2, -side/2)
turtle.pendown()
for _ in range(3):
    turtle.forward(side)
    turtle.left(120)
turtle.end_poly()
turtle.end_fill()

turtle.hideturtle()
turtle.done()