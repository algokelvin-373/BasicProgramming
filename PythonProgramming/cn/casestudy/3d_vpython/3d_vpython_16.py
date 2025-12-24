from vpython import *
import random, sys, platform

# ========= SOUND (2 nada) =========
IS_WIN = platform.system().lower().startswith("win")
if IS_WIN:
    import winsound

def beep(freq, ms):
    try:
        if IS_WIN:
            winsound.Beep(freq, ms)
        else:
            # fallback: bell (tidak beda nada di banyak terminal)
            sys.stdout.write("\a")
            sys.stdout.flush()
    except:
        pass

def sound_wall():
    beep(520, 35)   # wall: lebih rendah

def sound_ball():
    beep(1100, 25)  # ball: lebih tinggi

# ========= SCENE =========
scene.background = color.black
scene.width = 900
scene.height = 650
scene.userspin = True
scene.userzoom = True
scene.userpan  = True

scene.camera.pos  = vector(13, 9, 13)
scene.camera.axis = vector(-13, -9, -13)
scene.range = 11

# ========= KONFIG =========
ROOM_R = 10.0
BALL_R = 0.25
SPEED  = 0.02

MAX_BALLS = 120
SPAWN_TRIES = 80

# ========= RUANG BOLA (visual + grid) =========
room = sphere(pos=vector(0,0,0), radius=ROOM_R, opacity=0.06, color=color.white)

grid_color = color.gray(0.65)

# 3 ring utama (equator + 2 plane)
ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=ROOM_R, thickness=0.03, color=grid_color)
ring(pos=vector(0,0,0), axis=vector(1,0,0), radius=ROOM_R, thickness=0.03, color=grid_color)
ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=ROOM_R, thickness=0.03, color=grid_color)

# Latitude rings (lingkaran horizontal di berbagai ketinggian)
lat_steps = 7  # makin besar makin rapat
for k in range(1, lat_steps):
    y = ROOM_R * (2*k/lat_steps - 1) * 0.85   # scale biar tidak sampai kutub full (lebih estetik)
    r = sqrt(max(ROOM_R**2 - y**2, 0.0))
    if r > 0.2:
        ring(pos=vector(0, y, 0), axis=vector(0,1,0), radius=r, thickness=0.015, color=grid_color)

# Meridian rings (lingkaran vertikal diputar beberapa derajat)
meridians = 10
for m in range(meridians):
    ang = 2*pi*m/meridians
    axis = vector(cos(ang), 0, sin(ang))  # axis di bidang XZ
    ring(pos=vector(0,0,0), axis=axis, radius=ROOM_R, thickness=0.012, color=color.gray(0.5))

# ========= SIMULASI =========
balls = []

def random_point_inside_sphere(r_max):
    u = random.random()
    v = random.random()
    theta = 2*pi*u
    phi = acos(2*v - 1)
    rr = (random.random() ** (1/3)) * r_max
    return vector(
        rr * sin(phi) * cos(theta),
        rr * sin(phi) * sin(theta),
        rr * cos(phi)
    )

def spawn_ball():
    if len(balls) >= MAX_BALLS:
        return

    for _ in range(SPAWN_TRIES):
        p = random_point_inside_sphere(ROOM_R - BALL_R)

        ok = True
        for b in balls:
            if mag(b.pos - p) < 2*BALL_R:
                ok = False
                break
        if ok:
            b = sphere(
                pos=p,
                radius=BALL_R,
                color=vector(random.random(), random.random(), random.random()),
                shininess=0.9
            )
            b.v = vector(
                random.uniform(-SPEED, SPEED),
                random.uniform(-SPEED, SPEED),
                random.uniform(-SPEED, SPEED)
            )
            balls.append(b)
            return

# start 1 ball
spawn_ball()

def bounce_on_sphere_wall(b):
    boundary = ROOM_R - BALL_R
    dist = mag(b.pos)

    if dist > boundary:
        n = norm(b.pos)
        b.pos = n * boundary
        b.v = b.v - 2 * dot(b.v, n) * n
        return True
    return False

def resolve_ball_collision(b1, b2):
    r12 = b1.pos - b2.pos
    d = mag(r12)
    if d == 0:
        return False

    if d < 2*BALL_R:
        n = r12 / d
        overlap = 2*BALL_R - d

        # pisahkan biar tidak nempel
        b1.pos += n * (overlap/2)
        b2.pos -= n * (overlap/2)

        vrel = b1.v - b2.v
        vn = dot(vrel, n)
        if vn < 0:
            # equal mass elastic along normal
            b1.v -= vn * n
            b2.v += vn * n
            return True
    return False

# ========= LOOP =========
while True:
    rate(90)

    # move + wall collision
    for b in balls:
        b.pos += b.v
        if bounce_on_sphere_wall(b):
            sound_wall()
            spawn_ball()

    # ball-ball collision
    any_hit = False
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            if resolve_ball_collision(balls[i], balls[j]):
                any_hit = True

    if any_hit:
        sound_ball()
