GlowScript 2.4 VPython

#ground
ground =box(pos=vec(0,-0.05,0),size=vec(100,0.10,70), color = color.green)

#init. positon & velocity of ball
ball = sphere(pos=vec(0,0.11,0),radius=0.11, color = color.yellow, make_trail= True) #m
ball.m = 0.45 #kg
ball.speed = 32 #m/s
ball.angle = 20*pi/180
ball.v = ball.speed*vec(cos(ball.angle),sin(ball.angle),0)

wind_speed = 0 #m/s
wind_v = wind_speed*vec(1,0,0)

#graph object

#gd = graph(xmin = 0, xmax =20, ymin=-12, ymax=12)
gball_vy = gcurve()
gball_y = gcurve(color=color.cyan)
scale = 0.2
ball_vel = arrow(pos=ball.pos, axis=scale*ball.v, shaftwidth = 0.1)


#scene setting
#scene.autoscale = False
scene.range = 10

#const.
g = -9.8 #m/s**2
rho = 1.204 #kg/m**3
Cdl = 0.275#0.3#0.3#1 #laminar
Cdt = 0.05 # turbulent
w = 10*2*pi # angular speed #s**-1

#magnus param.
thold = 30 #m/s
Cml = 1 #laminar
Cmt = 0.05 # turbluent

#time setting
t = 0
dt = 0.01

scene.waitfor('click')
while t < 200:
    rate(100)
    #Gravity Force
    grav = ball.m * vec(0,g,0) #gravity

    #Drag Force & Magnus Force
    ball.v_w = ball.v - wind_v
    Cd = Cdl
    drag = -0.5*rho*Cd*(pi*ball.radius**2)*mag(ball.v_w)**2*norm(ball.v_w)
    magnus = 0.5*rho*Cml*(pi*ball.radius**2)*ball.radius*w*mag(ball.v_w)*cross(vec(0,1,0),norm(ball.v_w))

    #Sum of Forces
    ball.f = grav + drag + magnus
    print(mag(grav), mag(drag), mag(magnus))
    
    #Euler method: time stepping
    ball.v = ball.v + ball.f/ball.m*dt
    ball.pos = ball.pos + ball.v*dt
    ball_vel.pos = ball.pos
    ball_vel.axis = scale*ball.v

    #graph
    gball_vy.plot(pos=(t,mag(ball.v)))
    gball_y.plot(pos=(t,ball.pos.y))
    #collision
    if ball.pos.y - ball.radius < 0:
        print(ball.pos.x)
        break
    t = t + dt
    print(scale)
    t = t + dt
