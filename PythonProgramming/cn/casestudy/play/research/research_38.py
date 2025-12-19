from turtle import *

# =====================
# KONFIGURASI AWAL
# =====================
n = 80.0

screensize(bg="seashell")
hideturtle()
colormode(255)
speed(0)
goto(0, -200)

left(90)
forward(n)

# =====================
# GAMBAR BINTANG
# =====================
# color("orange", "yellow")
# begin_fill()
# left(126)
# for i in range(5):
#     forward(n / 5)
#     right(144)
#     forward(n / 5)
#     left(72)
# end_fill()
# right(126)

# =====================
# FUNGSI POHON FRACTAL
# =====================
color("dark green")

def tree(d, s):
    if d <= 0:
        return
    forward(s)
    tree(d - 1, s * 0.8)
    right(120)
    tree(d - 3, s * 0.5)
    right(120)
    tree(d - 3, s * 0.5)
    right(120)
    backward(s)

# =====================
# GAMBAR POHON
# =====================
tree(20, n)
backward(n / 2)

done()
