from vpython import *

# ============ SCENE ===========
scene.background = color.black
scene.width = 1000
scene.height = 700
scene.user_spin = True
scene.user_zoom = True
scene.user_pan = True

scene.camera.pos = vector(12, 8, 16)
scene.camera.axis = vector(-12, -6, -16)
scene.range = 14


# ============ FLOOR ===========
def create_floor(size=18, y=0):
    floor = box(
        pos=vector(0, y-0.05, 0),
        size=vector(size, 0.1, size),
        color=color.gray(0.15),
        opacity=0.9
    )

    grid_col = color.gray(0.35)
    step = 1.0

    for x in range(int(-size/2), int(size/2)+1):
        curve(
            pos=[
                vector(x, y, -size/2),
                vector(x, y, size/2)
            ],
            radius=0.015,
            color=grid_col
        )

    for z in range(int(-size/2), int(size/2)+1):
        curve(
            pos=[
                vector(-size/2, y, z),
                vector(size/2, y, z)
            ],
            radius=0.015,
            color=grid_col
        )

    # axis helpers (depth cue)
    arrow(
        pos=vector(0,y,0),
        axis=vector(4,0,0),
        shaftwidth=0.06, color=color.red
    )
    arrow(
        pos=vector(0,y,0),
        axis=vector(0,0,4),
        shaftwidth=0.06, color=color.blue
    )

    return floor


# ============ BALL ===========
def create_ball(radius=0.8, start_pos=vector(0,1,0)):
    core = sphere(
        pos=start_pos,
        radius=radius,
        color=color.cyan,
        shininess=0.9
    )

    marker = sphere(
        pos=start_pos + vector(0, 0.2, radius*0.92),
        radius=0.12,
        color=color.white
    )

    ball = compound([core, marker])
    ball.pos = start_pos
    ball.radius = radius
    return ball


def move_ball(ball, velocity, floor_y, limit):
    old_pos = vector(ball.pos.x, ball.pos.y, ball.pos.z)

    # translation
    ball.pos += velocity

    # area
    if ball.pos.x > limit:
        ball.pos.x = limit
        velocity.x *= -1
    elif ball.pos.x < -limit:
        ball.pos.x = -limit
        velocity.x *= -1

    if ball.pos.z > limit:
        ball.pos.z = limit
        velocity.z *= -1
    elif ball.pos.z < -limit:
        ball.pos.z = -limit
        velocity.z *= -1

    # rolling (without slip)
    dp = ball.pos - old_pos
    dist = mag(dp)

    if dist > 1e-6:
        up = vector(0,1,0)
        axis_rot = cross(up, norm(dp))
        angle = dist / ball.radius
        ball.rotate(angle=angle, axis=axis_rot, origin=ball.pos)

    return velocity


# ============ START: SETUP ===========
FLOOR_Y = 0
SIZE = 18
RADIUS = 0.8

create_floor(SIZE, FLOOR_Y)

ball = create_ball(
    radius=RADIUS,
    start_pos=vector(-6, FLOOR_Y + RADIUS, -3)
)

velocity = vector(0.08, 0, 0.05)
LIMIT = SIZE/2 - RADIUS - 0.2

while True: # Loop
    rate(60)
    velocity = move_ball(ball, velocity, FLOOR_Y, LIMIT)
# ============ END: SETUP ===========