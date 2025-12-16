from vpython import sphere, vector, rate, color, mag
import random

# ===== Configuration =====
N = 10
RADIUS = 0.5
LIMIT = 5
SPEED = 0.1

balls = []

# ===== Initialize ball =====
for i in range(N):
    ball = sphere(
        pos=vector(
            random.uniform(-LIMIT, LIMIT),
            random.uniform(-LIMIT, LIMIT),
            random.uniform(-LIMIT, LIMIT)
        ),
        radius=RADIUS,
        color=vector(random.random(), random.random(), random.random())
    )
    ball.v = vector(
        random.uniform(-SPEED, SPEED),
        random.uniform(-SPEED, SPEED),
        random.uniform(-SPEED, SPEED)
    )
    balls.append(ball)

# ===== Loop =====
while True:
    rate(60)

    # Gerak + pantul dinding
    for b in balls:
        b.pos += b.v

        if abs(b.pos.x) > LIMIT:
            b.v.x *= -1
        if abs(b.pos.y) > LIMIT:
            b.v.y *= -1
        if abs(b.pos.z) > LIMIT:
            b.v.z *= -1

    # Tabrakan antar bola
    for i in range(N):
        for j in range(i+1, N):
            b1 = balls[i]
            b2 = balls[j]

            if mag(b1.pos - b2.pos) < 2 * RADIUS:
                # Tukar velocity (elastic sederhana)
                b1.v, b2.v = b2.v, b1.v
