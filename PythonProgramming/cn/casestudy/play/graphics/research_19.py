import turtle

def bezier(t, p0, p1, p2):
    """Hitung titik pada kurva kuadrat Bézier"""
    x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
    y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
    return (x, y)

# Setup
screen = turtle.Screen()
screen.setup(800, 600)
screen.setworldcoordinates(-50, -50, 200, 250)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(2)
t.pensize(2)
t.color("purple")

# Titik
P0 = (0, 0)
P2 = (150, 100)
P1 = (75, 200)  # titik kontrol — semakin tinggi, semakin melengkung

# Tampilkan titik
t.penup()
t.goto(P0); t.dot(8, "green"); t.write(" P0")
t.goto(P1); t.dot(8, "gray"); t.write(" P1 (kontrol)")
t.goto(P2); t.dot(8, "red"); t.write(" P2")

# Hubungkan P0-P1 dan P1-P2 (garis bantu)
t.penup()
t.goto(P0)
t.pendown()
t.goto(P1)
t.penup()
t.goto(P1)
t.pendown()
t.goto(P2)
t.penup()

# Gambar kurva Bézier
t.color("blue")
t.pensize(3)
for i in range(101):
    t_bezier = i / 100  # t dari 0 ke 1
    x, y = bezier(t_bezier, P0, P1, P2)
    if i == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

t.hideturtle()
turtle.done()