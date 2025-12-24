from vpython import sphere, vector, rate, color

# ===== Scene =====
ball = sphere(
    pos=vector(0,0,0),
    radius=0.5,
    color=color.cyan
)
v = vector(0.02, 0.03, 0.01)

LIMIT = 5

while True:
    rate(60)
    ball.pos += v
    if abs(ball.pos.x) > LIMIT: # Bounce X
        v.x *= -1
    if abs(ball.pos.y) > LIMIT: # Bounce Y
        v.y *= -1
    if abs(ball.pos.z) > LIMIT: # Bounce Z
        v.z *= -1

    ball.rotate(angle=0.05, axis=vector(0,1,0))
