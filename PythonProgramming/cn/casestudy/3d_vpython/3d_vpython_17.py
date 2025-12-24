import math
from random import random

from vpython import *

# ===================== SCENE =====================
scene.background = color.black
scene.width = 1100
scene.height = 720

scene.userspin = True  # drag kiri = rotate
scene.userzoom = True  # scroll = zoom
scene.userpan = True  # drag kanan / shift+drag = pan

scene.camera.pos = vector(0, 25, 55)
scene.camera.axis = vector(0, -12, -55)
scene.range = 35

# ===================== SUN =====================
sun = sphere(pos=vector(0, 0, 0), radius=2.8, color=color.yellow, emissive=True)
local_light(pos=vector(0, 0, 0), color=color.white)


# ===================== HELPERS =====================
def rot_x(v, ang):
    c, s = math.cos(ang), math.sin(ang)
    return vector(v.x, v.y * c - v.z * s, v.y * s + v.z * c)


def rot_y(v, ang):
    c, s = math.cos(ang), math.sin(ang)
    return vector(v.x * c + v.z * s, v.y, -v.x * s + v.z * c)


def orbit_pos(a, e, theta):
    # posisi elips di bidang XZ (fokus di origin kira-kira ok untuk visual)
    r = a * (1 - e * e) / (1 + e * math.cos(theta))
    return vector(r * math.cos(theta), 0, r * math.sin(theta))


def make_orbit_curve(a, e, inc, node, npts=220):
    pts = []
    for k in range(npts + 1):
        th = 2 * math.pi * k / npts
        p = orbit_pos(a, e, th)
        p = rot_y(p, node)
        p = rot_x(p, inc)
        pts.append(p)
    return curve(pos=pts, color=color.gray(0.25), radius=0.02)


# ===================== PLANET DATA =====================
# name, a, e, inc(deg), node(deg), radius, period(years-ish), day(hours-ish), color, axial_tilt(deg)
planets_data = [
    ("Merkurius", 5.0, 0.206, 7.0, 0.0, 0.24, 0.240, 1407.6, color.gray(0.7), 0.0),
    ("Venus", 7.2, 0.007, 3.4, 25.0, 0.32, 0.615, -5832.5, vector(1.0, 0.8, 0.3), 177.0),
    ("Bumi", 9.8, 0.017, 0.0, 55.0, 0.34, 1.000, 24.0, vector(0.2, 0.5, 1.0), 23.4),
    ("Mars", 12.5, 0.093, 1.9, 80.0, 0.28, 1.880, 24.6, vector(1.0, 0.35, 0.2), 25.2),
    ("Jupiter", 17.0, 0.049, 1.3, 120.0, 0.95, 11.86, 9.9, vector(0.9, 0.7, 0.5), 3.1),
    ("Saturnus", 22.5, 0.057, 2.5, 155.0, 0.80, 29.46, 10.7, vector(0.95, 0.85, 0.6), 26.7),
    ("Uranus", 28.5, 0.046, 0.8, 205.0, 0.62, 84.01, -17.2, vector(0.6, 0.9, 0.95), 97.8),
    ("Neptunus", 33.0, 0.010, 1.8, 260.0, 0.60, 164.8, 16.1, vector(0.25, 0.45, 1.0), 28.3),
]

# ===================== CREATE PLANETS =====================
planets = []
labels = []
show_labels = True

for name, a, e, inc_deg, node_deg, rad, period, day_hours, col, tilt_deg in planets_data:
    inc = math.radians(inc_deg)
    node = math.radians(node_deg)
    tilt = math.radians(tilt_deg)

    # orbit curve (elips + inclination + node)
    make_orbit_curve(a, e, inc, node)

    # planet object
    p = sphere(radius=rad, color=col, shininess=0.85)
    p.name = name
    p.a = a
    p.e = e
    p.inc = inc
    p.node = node
    p.period = period
    p.theta = 2 * math.pi * random()  # start phase random

    # rotation (day)
    # skala kecepatan rotasi supaya enak dilihat:
    # (1/dayspeed) makin besar -> makin cepat muter
    p.day_hours = day_hours
    p.spin_speed = 0.6 * (24.0 / max(1e-6, abs(day_hours)))  # relatif ke Bumi
    p.spin_dir = 1 if day_hours >= 0 else -1

    # axial tilt: buat axis miring dari "atas" (y)
    # axis awal (0,1,0) kita miringkan ke arah x
    base_axis = vector(math.sin(tilt), math.cos(tilt), 0)
    # lalu rotasikan axis itu mengikuti node+inclination biar “nyambung” dengan orientasi orbit
    base_axis = rot_y(base_axis, node)
    base_axis = rot_x(base_axis, inc)
    p.spin_axis = norm(base_axis)

    # initial position
    pos0 = orbit_pos(a, e, p.theta)
    pos0 = rot_y(pos0, node)
    pos0 = rot_x(pos0, inc)
    p.pos = pos0

    # label
    lab = label(
        pos=p.pos,
        text=name,
        xoffset=10, yoffset=10,
        height=10,
        box=False,
        opacity=0,
        color=color.white
    )
    labels.append(lab)

    # Saturn rings
    if name == "Saturnus":
        p.rings = [
            ring(pos=p.pos, axis=p.spin_axis, radius=rad * 1.9, thickness=0.06, color=color.gray(0.65), opacity=0.6),
            ring(pos=p.pos, axis=p.spin_axis, radius=rad * 2.4, thickness=0.06, color=color.gray(0.55), opacity=0.5),
        ]
    else:
        p.rings = []

    planets.append(p)


# ===================== LABEL TOGGLE =====================
def keydown(evt):
    global show_labels
    k = evt.key
    if k.lower() == 'l':
        show_labels = not show_labels
        for lab in labels:
            lab.visible = show_labels


scene.bind('keydown', keydown)

# ===================== ANIMATION =====================
dt = 0.02
orbit_speed_scale = 0.1  # naikkan untuk orbit lebih cepat

while True:
    rate(60)

    for idx, p in enumerate(planets):
        # orbit step (theta)
        omega_orbit = (2 * math.pi / p.period) * dt * orbit_speed_scale
        p.theta += omega_orbit

        # posisi elips + orientasi orbit
        pos = orbit_pos(p.a, p.e, p.theta)
        pos = rot_y(pos, p.node)
        pos = rot_x(pos, p.inc)
        p.pos = pos

        # spin (day rotation)
        p.rotate(angle=p.spin_dir * p.spin_speed * dt, axis=p.spin_axis, origin=p.pos)

        # update label position
        labels[idx].pos = p.pos

        # update Saturn rings
        for r in p.rings:
            r.pos = p.pos
            r.axis = p.spin_axis
