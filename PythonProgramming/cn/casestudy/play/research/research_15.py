import turtle


def frange(start, stop, step):
    while start < stop:
        yield start
        start += step


# Setup layar
screen = turtle.Screen()
screen.setup(800, 600)
screen.setworldcoordinates(-10, -15, 10, 10)  # cukup ruang ke bawah untuk y=-15
screen.bgcolor("white")
screen.title("Grafik Kuadrat: y = ax² + bx - 5")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)


# Gambar sumbu X dan Y
def draw_axes():
    t.pencolor("gray")
    t.pensize(1)

    # Sumbu X
    t.penup()
    t.goto(-10, 0)
    t.pendown()
    t.goto(10, 0)

    # Sumbu Y
    t.penup()
    t.goto(0, -15)
    t.pendown()
    t.goto(0, 10)

    t.penup()
    t.goto(10.2, -0.5)
    t.write("X", font=("Arial", 12, "normal"))
    t.goto(-0.5, 10.2)
    t.write("Y", font=("Arial", 12, "normal"))


draw_axes()

# Parameter fungsi kuadrat
a = 1  # parabola terbuka ke atas
b = 0  # simetris di sumbu y
c = -5  # penting: agar saat x=0 → y = -5

# Tampilkan rumus
t.penup()
t.goto(-9, 8)
t.color("purple")
t.write(f"y = {a}x² + {b}x + ({c})", font=("Arial", 14, "bold"))

# Tandai titik (0, -5)
t.penup()
t.goto(0, -5)
t.dot(8, "red")
t.penup()
t.goto(0.5, -5.5)
t.color("red")
t.write("(0, -5)", font=("Arial", 12, "normal"))

# Gambar grafik
t.penup()
t.color("blue")
t.pensize(2)
first_point = True

for x in frange(-8, 8, 0.05):
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