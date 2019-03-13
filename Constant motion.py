GlowScript 2.5 VPython

track = box(pos=vector(0,0,0), length=6, width=0.1, height=0.05, color=color.blue)
cart=box(make_trail=True, pos=vector(-2.95, 0.06, 0), length=0.1, width=0.06, height=0.04,
color=color.green)
cart.velocity = vector(2,0,0)
dt = 0.01
time = 0
while time < 10:
    rate(100)
    cart.pos = cart.pos + cart.velocity*dt
    if -3 < cart.pos.x < 3:
        True
    else:
        cart.velocity = -cart.velocity
    time = time + dt
