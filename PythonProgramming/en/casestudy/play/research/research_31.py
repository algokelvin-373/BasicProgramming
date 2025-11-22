import turtle
import math


# Fungsi untuk menggambar elips
def draw_ellipse(x_center, y_center, radius_x, radius_y, tilt=0, steps=200):
    """
    Menggambar elips dengan pusat di (x_center, y_center),
    radius_x = sumbu mayor (horizontal),
    radius_y = sumbu minor (vertikal),
    tilt = kemiringan dalam derajat (opsional),
    steps = jumlah titik untuk menggambar (semakin banyak, semakin halus)
    """
    turtle.penup()
    # Pindah ke titik awal
    x = radius_x * math.cos(0)
    y = radius_y * math.sin(0)

    # Terapkan rotasi jika ada tilt
    if tilt != 0:
        rad_tilt = math.radians(tilt)
        x_rot = x * math.cos(rad_tilt) - y * math.sin(rad_tilt)
        y_rot = x * math.sin(rad_tilt) + y * math.cos(rad_tilt)
        x, y = x_rot, y_rot

    turtle.goto(x_center + x, y_center + y)
    turtle.pendown()

    # Gambar elips
    for i in range(1, steps + 1):
        t = 2 * math.pi * i / steps
        x = radius_x * math.cos(t)
        y = radius_y * math.sin(t)

        # Rotasi jika diperlukan
        if tilt != 0:
            rad_tilt = math.radians(tilt)
            x_rot = x * math.cos(rad_tilt) - y * math.sin(rad_tilt)
            y_rot = x * math.sin(rad_tilt) + y * math.cos(rad_tilt)
            x, y = x_rot, y_rot

        turtle.goto(x_center + x, y_center + y)


# Setup layar
screen = turtle.Screen()
screen.title("Menggambar Elips dengan Turtle")
screen.bgcolor("white")

# Setup turtle
t = turtle.Turtle()
t.speed(5)  # Kecepatan gambar (1-10, atau 0 untuk instan)

# Gambar elips
draw_ellipse(0, 0, 100, 50)  # Pusat di (0,0), lebar 200, tinggi 100
draw_ellipse(0, 0, 100, 50, tilt=45)

# Tutup jendela saat diklik
screen.exitonclick()