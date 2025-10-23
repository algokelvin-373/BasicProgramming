import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Segitiga Sierpinski")

# Setup turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()


def sierpinski_triangle(points, depth, t):
    """
    Menggambar segitiga Sierpinski secara rekursif.
    points: list dari 3 tuple (x, y) yang merepresentasikan titik sudut segitiga.
    depth: kedalaman rekursi.
    """
    # Gambar segitiga dasar
    draw_triangle(points, t, depth)

    if depth > 0:
        # Hitung titik tengah dari setiap sisi
        p0, p1, p2 = points
        mid01 = midpoint(p0, p1)
        mid12 = midpoint(p1, p2)
        mid20 = midpoint(p2, p0)

        # Rekursi pada 3 segitiga kecil di sudut
        sierpinski_triangle([p0, mid01, mid20], depth - 1, t)
        sierpinski_triangle([mid01, p1, mid12], depth - 1, t)
        sierpinski_triangle([mid20, mid12, p2], depth - 1, t)


def draw_triangle(points, t, depth):
    t.penup()
    t.goto(points[0])
    t.pendown()
    if depth == 0:
        t.color("red")
    else:
        t.color("black")
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])


def midpoint(p1, p2):
    """Menghitung titik tengah antara dua titik."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


# Titik awal segitiga besar (bisa disesuaikan)
# Contoh: segitiga sama sisi dengan tinggi vertikal
size = 800
top = (0, size / 2)
bottom_left = (-size / 2, -size / 2)
bottom_right = (size / 2, -size / 2)

# Mulai menggambar dengan kedalaman rekursi 5
sierpinski_triangle([top, bottom_left, bottom_right], 5, t)

# Tahan layar
screen.exitonclick()