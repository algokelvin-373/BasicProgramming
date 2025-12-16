from vpython import sphere, vector, rate, color

ball = sphere(
    pos=vector(3,2,1),
    radius=0.4,
    color=color.cyan
)
v = vector(0,0,0)

k = 0.01   # kekuatan tarik ke pusat
damp = 0.995

while True:
    rate(60)

    force = -k * ball.pos   # tarik ke pusat (0,0,0)
    v += force
    v *= damp   # redam
    ball.pos += v

    ball.rotate(angle=0.05, axis=vector(0,1,0))
