GlowScript 2.5 VPython

cart=box(pos=vec(0,0,0), length=0.5, width=1, height=0.3, color=color.green)
cart.v = vec(0,1,0)  # m/s
acc = vec(0,-2,0)
dt = 0.01  # sec
t = 0  # sec

cart_graph = gcurve(color=color.red)

while t < 3:
    rate(100)
    cart.v = cart.v+acc*dt
    cart.pos = cart.pos + cart.v*dt

    t = t + dt
    cart_graph.plot(pos=(t,cart.v.y))
