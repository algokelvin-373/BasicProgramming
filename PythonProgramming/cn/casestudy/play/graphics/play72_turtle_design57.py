import math
import turtle

def ellipse(
        x_center,
        y_center,
        radius_x,
        radius_y,
        tilt=0,
        steps=200
):
    turtle.penup()
    x = radius_x * math.cos(0)
    y = radius_y * math.sin(0)
    if tilt != 0:
        rad_tilt = math.radians(tilt)
        x_rot = x * math.cos(rad_tilt) - y * math.sin(rad_tilt)
        y_rot = x * math.sin(rad_tilt) + y * math.cos(rad_tilt)
        x, y = x_rot, y_rot
    turtle.goto(x_center + x, y_center + y)
    turtle.pendown()

    # Draw Ellipse
    for i in range(1, steps + 1):
        t = 2 * math.pi * i / steps
        x = radius_x * math.cos(t)
        y = radius_y * math.sin(t)

        if tilt != 0:
            rad_tilt = math.radians(tilt)
            x_rot = x * math.cos(rad_tilt) - y * math.sin(rad_tilt)
            y_rot = x * math.sin(rad_tilt) + y * math.cos(rad_tilt)
            x, y = x_rot, y_rot

        turtle.goto(x_center + x, y_center + y)

def design57(r, angle):
    tilt = 0
    for _ in range(int(180/angle)):
        ellipse(0, 0, r, r/2, tilt=tilt)
        tilt += angle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(2)
turtle.speed(0)

design57(200, 10)

turtle.hideturtle()
turtle.done()