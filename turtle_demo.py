import turtle
import random
import math

# ----------------------------
# Screen setup
# ----------------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(900, 900)
screen.title("Galaxy Simulation")
screen.tracer(0)

# ----------------------------
# Turtle setup
# ----------------------------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# ----------------------------
# Create background stars
# ----------------------------
star_colors = ["white", "lightblue", "lightyellow", "lightpink", "lightcyan"]

stars = []
for _ in range(700):
    angle = random.uniform(0, 360)
    radius = random.uniform(20, 400)
    speed = random.uniform(0.1, 1.5) * (1 if radius < 200 else 0.5)
    size = random.uniform(1, 4)
    color = random.choice(star_colors)
    twinkle_speed = random.uniform(0.02, 0.08)
    twinkle_phase = random.uniform(0, math.pi * 2)
    stars.append([angle, radius, speed, size, color, twinkle_speed, twinkle_phase])

# ----------------------------
# Black hole accretion disk particles
# ----------------------------
bh_x, bh_y = -300, 300  # black hole position (top-left area)
accretion_particles = []
for _ in range(150):
    angle = random.uniform(0, 360)
    radius = random.uniform(35, 90)
    speed = random.uniform(2, 6) * (90 / max(radius, 1))  # inner particles spin faster
    size = random.uniform(1, 3)
    accretion_particles.append([angle, radius, speed, size])

frame = 0

# ----------------------------
# Animation function
# ----------------------------
def animate():
    global frame
    t.clear()

    # --- background stars ---
    for star in stars:
        star[0] += star[2]
        x = math.cos(math.radians(star[0])) * star[1]
        y = math.sin(math.radians(star[0])) * star[1]

        twinkle = (math.sin(frame * star[5] + star[6]) + 1) / 2
        dynamic_size = star[3] * (0.5 + twinkle)

        t.penup()
        t.goto(x, y)
        t.dot(dynamic_size, star[4])

    # --- glowing pulsing sun with corona flares ---
    sun_pulse = (math.sin(frame * 0.05) + 1) / 2
    glow_size = 40 + sun_pulse * 15

    t.goto(0, 0)
    t.dot(glow_size + 30, "#2a1a00")
    t.dot(glow_size + 18, "#7a4a00")
    t.dot(glow_size + 8, "#ffae00")
    t.dot(glow_size, "yellow")

    # corona flare rays shooting outward, rotating slowly
    num_rays = 12
    for i in range(num_rays):
        ray_angle = (frame * 0.5) + (i * 360 / num_rays)
        ray_length = glow_size + 25 + math.sin(frame * 0.1 + i) * 15
        rx = math.cos(math.radians(ray_angle)) * ray_length
        ry = math.sin(math.radians(ray_angle)) * ray_length
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.pencolor("#ffcc33")
        t.pensize(2)
        t.goto(rx, ry)
        t.penup()

    # --- black hole with swirling accretion disk ---
    for p in accretion_particles:
        p[0] += p[2]
        px = bh_x + math.cos(math.radians(p[0])) * p[1]
        py = bh_y + math.sin(math.radians(p[0])) * p[1] * 0.4  # flattened ellipse for disk look

        # color shifts from orange (outer) to white-hot (inner)
        heat = 1 - (p[1] / 90)
        r = 255
        g = int(100 + heat * 155)
        b = int(heat * 200)
        color = f"#{r:02x}{g:02x}{b:02x}"

        t.penup()
        t.goto(px, py)
        t.dot(p[3], color)

    # event horizon (pure black circle) drawn last so it hides particles behind it
    t.goto(bh_x, bh_y)
    t.dot(45, "black")
    # thin glowing ring right at the edge
    t.dot(48, "#ff6600")
    t.dot(45, "black")

    screen.update()
    frame += 1
    screen.ontimer(animate, 16)

# ----------------------------
# Start animation
# ----------------------------
animate()
turtle.done()