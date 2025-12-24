import turtle
import time
import random

# ========== SETUP ==========
screen = turtle.Screen()
screen.setup(900, 650)
screen.title("Merry Christmas 2025")
screen.bgcolor("#0b1b2b")

ui = turtle.Turtle()
ui.hideturtle()
ui.speed(0)

writer = turtle.Turtle()
writer.hideturtle()
writer.speed(0)

decor = turtle.Turtle()
decor.hideturtle()
decor.speed(0)

def jump(pen, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

# ========== BACKGROUND SNOW ==========
def snow(count=160):
    decor.penup()
    for _ in range(count):
        decor.goto(
            random.randint(-430, 430),
            random.randint(-300, 300)
        )
        decor.dot(random.randint(2, 4), "white")
    decor.pendown()

# ========== BASIC SHAPES ==========
def rounded_rect(pen, x, y, w, h, r, fill, outline=None, pensize=2):
    if outline is None:
        outline = fill
    pen.pensize(pensize)
    pen.pencolor(outline)
    pen.fillcolor(fill)
    jump(pen, x, y)
    pen.setheading(0)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(w - 2*r); pen.circle(r, 90)
        pen.forward(h - 2*r); pen.circle(r, 90)
    pen.end_fill()

def rect(pen, x, y, w, h, fill):
    pen.fillcolor(fill)
    pen.pencolor(fill)
    jump(pen, x, y)
    pen.setheading(0)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(w); pen.left(90)
        pen.forward(h); pen.left(90)
    pen.end_fill()

# ========== CLIPBOARD ==========
def draw_clipboard():
    rounded_rect(ui, -260, -250, 520, 520, 24, "#b07a4a", "#6b3f1f", 3)
    rounded_rect(ui, -225, -220, 450, 460, 18, "#f6efe6", "#e6d8c8", 2)
    rounded_rect(ui, -70, 200, 140, 55, 16, "#c7ced6", "#8a939c", 2)
    rounded_rect(ui, -35, 212, 70, 30, 12, "#0b1b2b", "#0b1b2b", 1)

# ========== ANIMATED WRITING ==========
def animate_write(text, x, y, font, color, delay=0.06):
    writer.color(color)
    typed = ""
    for ch in text:
        typed += ch
        writer.clear()
        jump(writer, x, y)
        writer.write(typed, font=font)
        time.sleep(delay)

def write_static(text, x, y, font, color):
    writer.color(color)
    jump(writer, x, y)
    writer.write(text, font=font)

# ========== RUN ==========
snow()
draw_clipboard()

animate_write(
    "Merry Christmas",
    -165, 70,
    ("Courier", 30, "bold"),
    "#1f2937"
)
animate_write(
    "2025",
    -40, 20,
    ("Courier", 52, "bold"),
    "#d97706"
)

writer.clear()
write_static("Merry Christmas", -165, 70, ("Courier", 30, "bold"), "#1f2937")
write_static("2025", -40, 0, ("Courier", 50, "bold"), "#d97706")
write_static("and Happy New Year ✨", -175, -40, ("Courier", 20, "normal"), "#2563eb")

turtle.done()
