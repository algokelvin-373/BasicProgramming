import turtle
import time
import random

# =======================
# SETUP
# =======================
screen = turtle.Screen()
screen.setup(900, 650)
screen.title("Merry Christmas 2025 - Clipboard")
screen.bgcolor("#0b1b2b")  # background malam

ui = turtle.Turtle()
ui.hideturtle()
ui.speed(0)

writer = turtle.Turtle()
writer.hideturtle()
writer.speed(0)

def jump(pen, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def rounded_rect(pen, x, y, w, h, r, fill, outline=None, pensize=2):
    if outline is None:
        outline = fill
    pen.pensize(pensize)
    pen.pencolor(outline)
    pen.fillcolor(fill)
    jump(pen, x, y)
    pen.setheading(0)
    pen.begin_fill()
    # bawah
    pen.forward(w - 2*r); pen.circle(r, 90)
    # kanan
    pen.forward(h - 2*r); pen.circle(r, 90)
    # atas
    pen.forward(w - 2*r); pen.circle(r, 90)
    # kiri
    pen.forward(h - 2*r); pen.circle(r, 90)
    pen.end_fill()

def rect(pen, x, y, w, h, fill, outline=None, pensize=2):
    if outline is None:
        outline = fill
    pen.pensize(pensize)
    pen.pencolor(outline)
    pen.fillcolor(fill)
    jump(pen, x, y)
    pen.setheading(0)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(w); pen.left(90)
        pen.forward(h); pen.left(90)
    pen.end_fill()

# =======================
# CLIPBOARD DRAWING
# =======================
def draw_clipboard():
    # papan (board)
    rounded_rect(ui, -260, -250, 520, 520, 24, fill="#b07a4a", outline="#6b3f1f", pensize=3)

    # kertas di atas papan
    rounded_rect(ui, -225, -220, 450, 460, 18, fill="#f6efe6", outline="#e6d8c8", pensize=2)

    # clip metal
    rounded_rect(ui, -70, 200, 140, 55, 16, fill="#c7ced6", outline="#8a939c", pensize=2)
    # lubang clip kecil
    rounded_rect(ui, -35, 212, 70, 30, 12, fill="#0b1b2b", outline="#0b1b2b", pensize=1)

    # garis tipis seperti shadow kertas
    ui.pensize(2)
    ui.pencolor("#e3d4c3")
    jump(ui, -210, 205)
    ui.setheading(0)
    ui.forward(420)

def animate_write(text, x, y, font=("Courier", 28, "bold"), color="#0b1b2b",
                  delay=0.06, jitter=1.2):
    """
    Animasi menulis per karakter. Pakai clear+write biar terasa mengetik/ditulis.
    """
    writer.color(color)
    writer.penup()
    writer.goto(x, y)
    writer.pendown()

    typed = ""
    for ch in text:
        typed += ch
        writer.clear()
        # jitter kecil biar terasa "handwritten/marker"
        jx = random.uniform(-jitter, jitter)
        jy = random.uniform(-jitter, jitter)
        writer.goto(x + jx, y + jy)
        writer.write(typed, font=font)
        time.sleep(delay)

def draw_marker_tip():
    """
    Marker kecil di samping, biar vibe 'habis nulis' di clipboard.
    """
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    # body marker
    rect(pen, 210, -70, 35, 160, fill="#111827", outline="#111827", pensize=1)
    # cap
    rect(pen, 210, 70, 35, 40, fill="#374151", outline="#374151", pensize=1)
    # tip
    pen.pencolor("#9ca3af")
    pen.fillcolor("#9ca3af")
    jump(pen, 217, -90)
    pen.setheading(-90)
    pen.begin_fill()
    pen.forward(25)
    pen.left(90); pen.forward(21)
    pen.left(90); pen.forward(25)
    pen.end_fill()

# =======================
# RUN
# =======================
draw_clipboard()

# Animasi teks seperti ditulis di kertas
animate_write("Merry Christmas", x=-165, y=70, font=("Courier", 30, "bold"), color="#1f2937", delay=0.07)
animate_write("2025", x=-40, y=20, font=("Courier", 52, "bold"), color="#d97706", delay=0.09, jitter=0.8)

# subtext kecil
animate_write("and Happy New Year ✨", x=-175, y=-40, font=("Courier", 20, "normal"),
              color="#2563eb", delay=0.05, jitter=1.0)

draw_marker_tip()

turtle.done()
