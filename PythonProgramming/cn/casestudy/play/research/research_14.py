import turtle


# Fungsi bantu untuk loop float
def frange(start, stop, step):
    """Generator untuk range dengan float"""
    while start < stop:
        yield start
        start += step


# Setup layar
screen = turtle.Screen()
screen.setup(800, 600)
screen.setworldcoordinates(-10, -20, 10, 20)  # x: -10..10, y: -20..20
screen.bgcolor("white")
screen.title("Grafik Kuadrat Halus: y = ax² + bx + c")

# Buat turtle
t = turtle.Turtle()
t.speed(0)  # Kecepatan maksimal
t.pensize(2)
t.color("blue")


# Gambar sumbu X dan Y
def draw_axes():
    t.pencolor("black")
    t.pensize(1)

    # Sumbu X
    t.penup()
    t.goto(-10, 0)
    t.pendown()
    t.goto(10, 0)

    # Sumbu Y
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.goto(0, 20)

    # Tanda panah (opsional)
    t.penup()
    t.goto(10.5, 0)
    t.write("X", font=("Arial", 12, "normal"))
    t.goto(0, 20.5)
    t.write("Y", font=("Arial", 12, "normal"))


#draw_axes()

# Parameter fungsi kuadrat: y = ax² + bx + c
a, b, c = 1, 0, 0  # Contoh: y = x²

# Label fungsi
t.penup()
t.goto(-9, 18)
t.color("purple")
t.write(f"y = {a}x² + {b}x + {c}", font=("Arial", 14, "bold"))

# Gambar grafik dengan langkah sangat kecil
t.penup()
t.pensize(2)
t.color("red")

first_point = True
x_min, x_max = -4, 4
step = 0.05  # Semakin kecil step → semakin halus! (0.01 lebih halus tapi lebih lambat)

for x in frange(x_min, x_max, step):
    y = a * x ** 2 + b * x + c

    if first_point:
        t.penup()
        t.goto(x, y)
        t.pendown()
        first_point = False
    else:
        t.goto(x, y)

t.hideturtle()
turtle.done()