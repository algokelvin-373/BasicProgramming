import turtle
import random

# ====== Setup ======
screen = turtle.Screen()
screen.title("Pohon Cemara - Natal & Tahun Baru")
screen.bgcolor("#0b1b2b")  # langit malam

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def jump(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def circle_dot(x, y, r, color):
    jump(x, y)
    pen.dot(r, color)

# ====== Salju ======
def snow(count=120):
    for _ in range(count):
        x = random.randint(-330, 330)
        y = random.randint(-220, 280)
        size = random.randint(2, 4)
        circle_dot(x, y, size, "white")

# ====== Bintang ======
def star(x, y, size=35, color="gold"):
    jump(x, y)
    pen.color(color)
    pen.begin_fill()
    pen.setheading(90)
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
        pen.forward(size)
        pen.left(72)
    pen.end_fill()

# ====== Segitiga daun cemara ======
def filled_triangle(x, y, width, height, color):
    jump(x, y)
    pen.color(color)
    pen.begin_fill()
    pen.setheading(0)
    pen.forward(width/2)
    pen.goto(x, y + height)
    pen.goto(x - width/2, y)
    pen.goto(x, y)
    pen.end_fill()

# ====== Batang ======
def trunk(x, y, w=60, h=70, color="#8b5a2b"):
    jump(x - w/2, y)
    pen.color(color)
    pen.begin_fill()
    pen.setheading(0)
    pen.forward(w)
    pen.left(90); pen.forward(h)
    pen.left(90); pen.forward(w)
    pen.left(90); pen.forward(h)
    pen.end_fill()

# ====== Hiasan bola ======
def ornaments(center_x, base_y, layers):
    colors = ["red", "gold", "deepskyblue", "hotpink", "orange", "white"]
    for i, (w, h) in enumerate(layers):
        # area segitiga layer
        y_bottom = base_y + sum(l[1] for l in layers[:i])
        y_top = y_bottom + h
        # pasang beberapa bola acak di dalam area segitiga
        for _ in range(8):
            y = random.randint(int(y_bottom + 10), int(y_top - 10))
            # lebar segitiga menyempit ke atas
            t = (y - y_bottom) / h
            half = (w/2) * (1 - t)
            x = random.randint(int(center_x - half + 10), int(center_x + half - 10))
            circle_dot(x, y, random.randint(10, 14), random.choice(colors))

# ====== Gambar Pohon ======
def draw_tree(center_x=0, base_y=-220):
    # salju
    snow(140)

    # tanah salju
    pen.color("#e8f1ff")
    jump(-400, -240)
    pen.begin_fill()
    pen.goto(400, -240)
    pen.goto(400, -170)
    pen.goto(-400, -170)
    pen.goto(-400, -240)
    pen.end_fill()

    # layer daun (bisa kamu ubah biar lebih tinggi/pendek)
    layers = [
        (140, 90),
        (190, 105),
        (240, 120),
        (290, 135),
    ]

    # gambar layer dari bawah ke atas
    current_y = base_y
    greens = ["#0b6b3a", "#0a5c33", "#0c7a41", "#0a6236"]
    for i, (w, h) in enumerate(layers[::-1]):  # mulai dari yang paling besar (bawah)
        filled_triangle(center_x, current_y, w, h, greens[i % len(greens)])
        current_y += int(h * 0.65)  # overlap supaya lebih "cemara"

    # batang
    trunk(center_x, base_y - 40, w=70, h=80)

    # hiasan
    # pakai urutan layer dari bawah ke atas untuk posisi hiasan
    ornaments(center_x, base_y + 10, [(290, 135), (240, 120), (190, 105), (140, 90)])

    # bintang di puncak (posisi kira-kira)
    star(center_x, base_y + 300, size=32)

    # lampu kelap-kelip (titik kecil)
    for _ in range(70):
        x = random.randint(-160, 160)
        y = random.randint(-120, 220)
        if random.random() < 0.55:
            circle_dot(x, y, 4, random.choice(["yellow", "white", "gold"]))

    # tulisan
    jump(-260, 230)
    pen.color("white")
    pen.write("Selamat Natal & Tahun Baru!", font=("Arial", 22, "bold"))

    jump(-215, 200)
    pen.color("#cfe8ff")
    pen.write("Semoga hangat, damai, dan penuh harapan ✨", font=("Arial", 14, "normal"))

draw_tree()

turtle.done()
