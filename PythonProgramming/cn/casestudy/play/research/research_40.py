import turtle
import random

# ======================
# SETUP LAYAR
# ======================
screen = turtle.Screen()
screen.title("Natal & Tahun Baru 🎄❄️🎁")
screen.bgcolor("#0b1b2b")
screen.setup(width=900, height=600)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)
turtle.colormode(255)

# ======================
# HELPER
# ======================
def jump(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# ======================
# BACKGROUND SALJU
# ======================
def snow(count=160):
    t.penup()
    for _ in range(count):
        t.goto(random.randint(-430, 430), random.randint(-260, 290))
        t.dot(random.randint(2, 4), "white")
    t.pendown()

def ground():
    t.color("#e8f1ff")
    jump(-450, -260)
    t.begin_fill()
    t.goto(450, -260)
    t.goto(450, -180)
    t.goto(-450, -180)
    t.goto(-450, -260)
    t.end_fill()

# ======================
# KADO
# ======================
def rect(x, y, w, h, fill, outline=None):
    jump(x, y)
    t.fillcolor(fill)
    t.pencolor(outline if outline else fill)
    t.setheading(0)
    t.begin_fill()
    for _ in range(2):
        t.forward(w); t.left(90)
        t.forward(h); t.left(90)
    t.end_fill()

def ribbon_vertical(x, y, w, h, color):
    rw = max(6, int(w * 0.18))
    rect(x + (w - rw)/2, y, rw, h, color)

def ribbon_horizontal(x, y, w, h, color):
    rh = max(6, int(h * 0.22))
    rect(x, y + (h - rh)/2, w, rh, color)

def bow(x, y, w, h, color):
    t.color(color)
    cx = x + w/2
    top = y + h
    jump(cx, top + 6)
    t.begin_fill()
    t.circle(4)
    t.end_fill()

def gift(x, y, w, h, box, ribbon):
    rect(x, y, w, h, box, "#0b1b2b")
    lid = max(8, int(h * 0.22))
    rect(x-2, y+h-lid+2, w+4, lid, box, "#0b1b2b")
    ribbon_vertical(x, y, w, h, ribbon)
    ribbon_horizontal(x, y, w, h, ribbon)
    bow(x, y+h-lid+2, w, lid, ribbon)

def draw_gifts():
    base_y = -240
    boxes = ["#e74c3c", "#3498db", "#f39c12", "#9b59b6", "#2ecc71"]
    ribbons = ["#ffffff", "#f1c40f", "#1abc9c"]

    positions = [(-280, base_y), (-150, base_y+5), (-20, base_y),
                 (120, base_y-5), (260, base_y)]

    for x, y in positions:
        gift(x, y,
             random.randint(70, 110),
             random.randint(45, 70),
             random.choice(boxes),
             random.choice(ribbons))

# ======================
# POHON NATAL FRACTAL
# ======================
def tree(depth, length):
    if depth <= 0:
        return
    t.forward(length)
    tree(depth-1, length*0.8)
    t.right(120)
    tree(depth-3, length*0.5)
    t.right(120)
    tree(depth-3, length*0.5)
    t.right(120)
    t.backward(length)

def draw_tree():
    t.color("dark green")
    jump(0, -180)
    t.setheading(90)
    tree(20, 80)

# ======================
# SCENE
# ======================
snow()
ground()
draw_gifts()
draw_tree()

turtle.done()
