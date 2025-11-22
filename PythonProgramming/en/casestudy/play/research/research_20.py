import turtle
import math


def rotate_point(x, y, angle_degrees):
    """Rotasi titik (x,y) sebesar angle_degrees terhadap (0,0)"""
    angle_rad = math.radians(angle_degrees)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    x_new = x * cos_a - y * sin_a
    y_new = y * sin_a + x * cos_a
    return (x_new, y_new)


def bezier(t, p0, p1, p2):
    """Kurva Bézier kuadrat"""
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return (x, y)


# Setup layar
screen = turtle.Screen()
screen.setup(800, 600)
screen.setworldcoordinates(-200, -200, 200, 200)
screen.bgcolor("white")
screen.title("Rotasi P1 terhadap (0,0)")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Titik tetap
P0 = (-100, 0)
P2 = (100, 0)

# Titik kontrol awal (sebelum rotasi)
P1_original = (0, 100)  # misalnya langsung di atas (0,0)

# Daftar sudut rotasi
angles = [0, 30, 60, 90, -30, -60]

# Gambar sumbu X dan Y
t.penup()
t.goto(-200, 0)
t.pendown()
t.goto(200, 0)
t.penup()
t.goto(0, -200)
t.pendown()
t.goto(0, 200)

for angle in angles:
    # Rotasi P1 terhadap (0,0)
    P1_rotated = rotate_point(P1_original[0], P1_original[1], angle)

    # Warna berbeda tiap sudut
    colors = {
        0: "blue",
        30: "green",
        60: "orange",
        90: "red",
        -30: "purple",
        -60: "brown"
    }
    t.color(colors.get(angle, "gray"))

    # Tampilkan titik P1 yang sudah dirotasi
    t.penup()
    t.goto(P1_rotated)
    t.dot(6, t.color()[0])
    if angle == 0:
        t.write(f" P1 ({angle}°)", align="left", font=("Arial", 10, "normal"))

    # Gambar kurva Bézier
    t.penup()
    for i in range(101):
        t_val = i / 100
        x, y = bezier(t_val, P0, P1_rotated, P2)
        if i == 0:
            t.penup()
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)

# Tandai titik penting
t.penup()
t.goto(P0)
t.dot(8, "black")
t.write(" P0", align="left")

t.goto(P2)
t.dot(8, "black")
t.write(" P2", align="right")

t.hideturtle()
turtle.done()