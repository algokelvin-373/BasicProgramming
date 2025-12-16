import turtle
import random

# ====== Setup ======
screen = turtle.Screen()
screen.title("Background Natal + Kado")
screen.bgcolor("#0b1b2b")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

def jump(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def rect(x, y, w, h, fill, outline=None):
    jump(x, y)
    if outline is None:
        outline = fill
    t.pencolor(outline)
    t.fillcolor(fill)
    t.setheading(0)
    t.begin_fill()
    for _ in range(2):
        t.forward(w); t.left(90)
        t.forward(h); t.left(90)
    t.end_fill()

def snow(count=140):
    t.penup()
    for _ in range(count):
        t.goto(random.randint(-330, 330), random.randint(-220, 280))
        t.dot(random.randint(2, 4), "white")
    t.pendown()

def ground():
    t.pencolor("#e8f1ff")
    t.fillcolor("#e8f1ff")
    jump(-400, -240)
    t.begin_fill()
    t.goto(400, -240)
    t.goto(400, -170)
    t.goto(-400, -170)
    t.goto(-400, -240)
    t.end_fill()

# ====== Gift Drawing ======
def ribbon_vertical(x, y, w, h, color):
    # pita vertikal (lebih tipis)
    rw = max(6, int(w * 0.18))
    rx = x + (w - rw) / 2
    rect(rx, y, rw, h, fill=color, outline=color)

def ribbon_horizontal(x, y, w, h, color):
    # pita horizontal
    rh = max(6, int(h * 0.22))
    ry = y + (h - rh) / 2
    rect(x, ry, w, rh, fill=color, outline=color)

def bow(x, y, w, h, color):
    # pita atas sederhana: 2 loop + knot
    t.pencolor(color)
    t.fillcolor(color)

    cx = x + w / 2
    top = y + h

    # knot
    jump(cx, top + 6)
    t.begin_fill()
    t.circle(4)
    t.end_fill()

    # loop kiri
    jump(cx - 8, top + 6)
    t.setheading(135)
    t.begin_fill()
    for _ in range(2):
        t.forward(14); t.right(90)
        t.forward(10); t.right(90)
    t.end_fill()

    # loop kanan
    jump(cx + 8, top + 6)
    t.setheading(45)
    t.begin_fill()
    for _ in range(2):
        t.forward(14); t.left(90)
        t.forward(10); t.left(90)
    t.end_fill()

def gift(x, y, w, h, box_color, ribbon_color):
    # kotak utama
    rect(x, y, w, h, fill=box_color, outline="#0b1b2b")  # outline gelap biar tegas
    # tutup (lid)
    lid_h = max(8, int(h * 0.22))
    rect(x - 2, y + h - lid_h + 2, w + 4, lid_h, fill=box_color, outline="#0b1b2b")

    # pita silang
    ribbon_vertical(x, y, w, h, ribbon_color)
    ribbon_horizontal(x, y, w, h, ribbon_color)

    # pita atas (bow)
    bow(x, y + h - lid_h + 2, w, lid_h, ribbon_color)

def draw_gifts():
    # area ground kira-kira y = -170..-240
    base_y = -230
    palette_boxes = ["#e74c3c", "#3498db", "#f39c12", "#9b59b6", "#2ecc71", "#e67e22"]
    palette_ribbon = ["#ecf0f1", "#f1c40f", "#1abc9c", "#ffffff", "#ffccd5"]

    # beberapa kado manual + random supaya komposisi bagus
    fixed = [
        (-260, base_y, 90, 60),
        (-150, base_y + 5, 70, 50),
        (-60,  base_y - 5, 110, 70),
        (90,   base_y + 0, 80, 55),
        (200,  base_y - 8, 95, 65),
    ]

    for (x, y, w, h) in fixed:
        gift(
            x, y, w, h,
            box_color=random.choice(palette_boxes),
            ribbon_color=random.choice(palette_ribbon)
        )

    # tambahan kecil-kecil di depan
    for _ in range(4):
        w = random.randint(45, 70)
        h = random.randint(35, 55)
        x = random.randint(-320, 260)
        y = random.randint(-238, -210)
        gift(x, y, w, h, random.choice(palette_boxes), random.choice(palette_ribbon))

def draw_scene():
    snow(150)
    ground()
    draw_gifts()

draw_scene()
turtle.done()
