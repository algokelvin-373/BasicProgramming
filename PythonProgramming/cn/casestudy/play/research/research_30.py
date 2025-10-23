import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dragon Curve - Fraktal Naga")

# Setup turtle
t = turtle.Turtle()
t.speed(0)
t.color("red")
t.hideturtle()

# Nonaktifkan animasi untuk kecepatan (opsional)
# screen.tracer(0, 0)


def dragon_curve(length, depth, turn_right=True):
    """
    Menggambar Dragon Curve secara rekursif.

    Parameter:
    - length: panjang segmen dasar
    - depth: kedalaman rekursi
    - turn_right: arah belok saat rekursi (True = kanan, False = kiri)
    """
    if depth == 0:
        t.forward(length)
        return

    # Setengah panjang untuk rekursi
    new_length = length / (2 ** 0.5)  # Menjaga ukuran tetap proporsional

    # Belok kiri atau kanan tergantung arah
    if turn_right:
        t.right(45)
    else:
        t.left(45)

    # Rekursi pertama
    dragon_curve(new_length, depth - 1, True)

    # Belok ke arah berlawanan
    if turn_right:
        t.left(90)
    else:
        t.right(90)

    # Rekursi kedua
    dragon_curve(new_length, depth - 1, False)

    # Kembali ke orientasi semula
    if turn_right:
        t.right(45)
    else:
        t.left(45)


# Atur parameter
depth = 12  # Kedalaman rekursi (8–14 biasanya bagus)
initial_length = 200

# Posisi awal agar muat di layar
t.penup()
t.goto(0, 0)
t.pendown()
t.right(45)  # Rotasi awal agar simetris

# Mulai menggambar!
dragon_curve(initial_length, depth)

# Perbarui layar
screen.update()

# Tahan layar
screen.exitonclick()