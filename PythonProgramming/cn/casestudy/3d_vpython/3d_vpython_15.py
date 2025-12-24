from vpython import *
import random

# ===== Scene =====
scene.background = color.black
scene.width = 900
scene.height = 650

# Pastikan interaksi camera aktif
scene.userspin = True   # drag kiri = rotate
scene.userzoom = True   # scroll = zoom
scene.userpan  = True   # drag kanan/shift = pan

# Kamera awal biar 3D langsung kebaca
scene.camera.pos  = vector(9, 7, 9)
scene.camera.axis = vector(-9, -7, -9)
scene.range = 7

# ===== Konfigurasi =====
N = 12
RADIUS = 0.35
LIMIT = 5
SPEED = 0.06

# ===== Kotak ruang =====
room = box(pos=vector(0,0,0),
           size=vector(2*LIMIT, 2*LIMIT, 2*LIMIT),
           opacity=0.08,
           color=color.white)

# Wireframe
curve(pos=[vector(-LIMIT,-LIMIT,-LIMIT), vector(LIMIT,-LIMIT,-LIMIT),
           vector(LIMIT,-LIMIT,LIMIT), vector(-LIMIT,-LIMIT,LIMIT),
           vector(-LIMIT,-LIMIT,-LIMIT)], color=color.gray(0.7))
curve(pos=[vector(-LIMIT,LIMIT,-LIMIT), vector(LIMIT,LIMIT,-LIMIT),
           vector(LIMIT,LIMIT,LIMIT), vector(-LIMIT,LIMIT,LIMIT),
           vector(-LIMIT,LIMIT,-LIMIT)], color=color.gray(0.7))
for x in (-LIMIT, LIMIT):
    for z in (-LIMIT, LIMIT):
        curve(pos=[vector(x,-LIMIT,z), vector(x,LIMIT,z)], color=color.gray(0.7))

# ===== Bola =====
balls = []
for _ in range(N):
    b = sphere(
        pos=vector(
            random.uniform(-LIMIT+RADIUS, LIMIT-RADIUS),
            random.uniform(-LIMIT+RADIUS, LIMIT-RADIUS),
            random.uniform(-LIMIT+RADIUS, LIMIT-RADIUS),
        ),
        radius=RADIUS,
        color=vector(random.random(), random.random(), random.random()),
        shininess=0.8
    )
    b.v = vector(
        random.uniform(-SPEED, SPEED),
        random.uniform(-SPEED, SPEED),
        random.uniform(-SPEED, SPEED)
    )
    balls.append(b)

# ===== Loop =====
while True:
    rate(60)

    for b in balls:
        b.pos += b.v

        for axis in ('x', 'y', 'z'):
            if getattr(b.pos, axis) > LIMIT - RADIUS:
                setattr(b.pos, axis, LIMIT - RADIUS)
                setattr(b.v, axis, -getattr(b.v, axis))
            elif getattr(b.pos, axis) < -LIMIT + RADIUS:
                setattr(b.pos, axis, -LIMIT + RADIUS)
                setattr(b.v, axis, -getattr(b.v, axis))

    for i in range(N):
        for j in range(i+1, N):
            b1, b2 = balls[i], balls[j]
            if mag(b1.pos - b2.pos) < 2*RADIUS:
                b1.v, b2.v = b2.v, b1.v
