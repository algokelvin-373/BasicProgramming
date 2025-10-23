import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Hilbert Curve - Space-Filling Fractal")

# Setup turtle
t = turtle.Turtle()
t.speed(0)
t.color("lime")
t.hideturtle()

# Nonaktifkan animasi untuk kecepatan maksimal (opsional)
# screen.tracer(0, 0)


def hilbert_curve(n, angle, step):
    """
    Menggambar Hilbert Curve secara rekursif.

    Parameter:
    - n: kedalaman rekursi (order)
    - angle: sudut belok (biasanya 90 derajat)
    - step: panjang setiap segmen
    """
    if n == 0:
        return

    # Putar kiri
    t.left(angle)
    hilbert_curve(n - 1, -angle, step)

    # Maju
    t.forward(step)

    # Putar kanan
    t.right(angle)
    hilbert_curve(n - 1, angle, step)

    # Maju lagi
    t.forward(step)

    # Rekursi lagi
    hilbert_curve(n - 1, angle, step)

    # Putar kanan
    t.right(angle)
    t.forward(step)

    # Rekursi terakhir
    hilbert_curve(n - 1, -angle, step)

    # Putar kiri
    t.left(angle)


# Atur parameter
order = 5  # Kedalaman rekursi (coba 3–6)
step_size = 8  # Panjang tiap langkah

# Posisi awal agar kurva berada di tengah
t.penup()
t.goto(- (2 ** order - 1) * step_size / 2, - (2 ** order - 1) * step_size / 2)
t.pendown()

# Mulai menggambar!
hilbert_curve(order, 90, step_size)

# Perbarui layar (karena pakai tracer)
screen.update()

# Tahan layar
screen.exitonclick()