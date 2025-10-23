import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")  # Latar belakang hitam agar salju terlihat kontras
screen.title("Koch Snowflake - Fraktal Salju")

# Setup turtle
t = turtle.Turtle()
t.speed(0)  # Kecepatan maksimum
t.color("cyan")
t.hideturtle()
t.penup()
t.goto(-150, 100)  # Posisi awal agar muat di layar
t.pendown()

def koch_curve(length, depth):
    """
    Menggambar satu sisi fraktal Koch secara rekursif.
    Jika depth = 0, gambar garis lurus.
    Jika depth > 0, ganti garis dengan pola Koch.
    """
    if depth == 0:
        t.forward(length)
    else:
        koch_curve(length / 3, depth - 1)
        t.left(60)
        koch_curve(length / 3, depth - 1)
        t.right(120)
        koch_curve(length / 3, depth - 1)
        t.left(60)
        koch_curve(length / 3, depth - 1)

def koch_snowflake(length, depth):
    """
    Menggambar Koch Snowflake lengkap: 3 sisi Koch Curve membentuk segitiga.
    """
    for _ in range(3):
        koch_curve(length, depth)
        t.right(120)

# Mulai menggambar!
# Panjang sisi awal: 300, kedalaman rekursi: 4
koch_snowflake(300, 5)

# Tahan layar
screen.exitonclick()