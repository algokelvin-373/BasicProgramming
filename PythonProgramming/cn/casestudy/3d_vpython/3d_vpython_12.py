from vpython import sphere, vector, rate, color
import math

ball = sphere(radius=0.4, color=color.cyan)

t = 0
R = 4   # jarak maksimum dari pusat
speed = 0.02

while True:
    rate(60)
    t += speed

    ball.pos = vector(
        R * math.sin(t),
        R * math.sin(t * 0.7),
        R * math.cos(t)
    )

    ball.rotate(angle=0.05, axis=vector(0,1,0))
