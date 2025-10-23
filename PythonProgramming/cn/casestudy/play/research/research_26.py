import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Fraktal Pohon Rekursif")

# Setup turtle
t = turtle.Turtle()
t.speed(0)  # Kecepatan maksimum
t.left(90)  # Hadap ke atas
t.penup()
t.goto(0, -200)  # Mulai dari bawah
t.pendown()
t.color("brown")


def draw_tree(branch_len, t, depth):
    if depth > 0:
        # Gambar cabang utama
        t.forward(branch_len)

        # Simpan posisi dan heading sebelum rekursi
        pos = t.position()
        head = t.heading()

        # Cabang kiri
        t.left(30)
        draw_tree(branch_len * 0.7, t, depth - 1)

        # Kembali ke posisi sebelumnya
        t.penup()
        t.setposition(pos)
        t.setheading(head)
        t.pendown()

        # Cabang kanan
        t.right(30)
        draw_tree(branch_len * 0.7, t, depth - 1)

        # Kembali ke posisi awal cabang
        t.penup()
        t.setposition(pos)
        t.setheading(head)
        t.pendown()


# Mulai menggambar dengan panjang awal 100 dan kedalaman rekursi 6
draw_tree(150, t, 10)

# Sembunyikan turtle dan tahan layar
t.hideturtle()
screen.exitonclick()