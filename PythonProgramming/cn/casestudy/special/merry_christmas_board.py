import turtle
import time
import random

# ========== SETUP ==========
screen = turtle.Screen()
screen.setup(900, 650)
screen.title("Merry Christmas 2025")
screen.bgcolor("#0b1b2b")
screen.tracer(0)

ui = turtle.Turtle()
ui.hideturtle()
ui.speed(0)

writer = turtle.Turtle()
writer.hideturtle()
writer.speed(0)

snow_pen = turtle.Turtle()
snow_pen.hideturtle()
snow_pen.speed(0)

# ========= HELPERS ==========
def jump(pen, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

# ========== LIVE SNOW ==========
snowflakes = []

def init_snow(count=120):
    for _ in range(count):
        snowflakes.append([
            random.randint(-450, 450),
            random.randint(-320, 320),
            random.randint(2, 4),
            random.uniform(0.6, 1.6)
        ])

def animate_snow():
    snow_pen.clear()
    for flake in snowflakes:
        flake[1] -= flake[3]
        if flake[1] < -330:
            flake[0] = random.randint(-450, 450)
            flake[1] = 330
        snow_pen.penup()
        snow_pen.goto(flake[0], flake[1])
        snow_pen.dot(flake[2], "white")
    screen.update()
    screen.ontimer(animate_snow, 50)

# ========== HANDWRITTEN WRITE ==========
def animate_write(text, x, y, font, color,
                  delay=0.06, jitter=1.2):
    writer.color(color)
    typed = ""
    for ch in text:
        typed += ch
        writer.clear()
        jump(
            writer,
            x + random.uniform(-jitter, jitter),
            y + random.uniform(-jitter, jitter)
        )
        writer.write(typed, font=font)
        screen.update()
        time.sleep(delay)

def write_static(text, x, y, font, color):
    writer.color(color)
    jump(writer, x, y)
    writer.write(text, font=font)

# ========== RUN ==========
init_snow()
animate_snow()

txt_data = [
    [
        "Merry Christmas",
        -165,
        80,
        ("Courier", 30, "italic"),
        "#ff0000"
    ],
    [
        "2025",
        -40,
        0,
        ("Courier", 50, "bold"),
        "#d97706",
        0.8
    ],
]

animate_write(
    txt_data[0][0],
    txt_data[0][1],
    txt_data[0][2],
    txt_data[0][3],
    txt_data[0][4]
)

animate_write(
    txt_data[1][0],
    txt_data[1][1],
    txt_data[1][2],
    txt_data[1][3],
    txt_data[1][4],
    jitter=txt_data[1][5]
)

writer.clear()

write_static(
    txt_data[0][0],
    txt_data[0][1],
    txt_data[0][2],
    txt_data[0][3],
    txt_data[0][4]
)
write_static(
    txt_data[1][0],
    txt_data[1][1],
    txt_data[1][2],
    txt_data[1][3],
    txt_data[1][4],
)

screen.update()
turtle.done()
