GlowScript 2.4 VPython

## objects
ceiling = box(pos=vector(0,0,0), opacity = 1,size = vector(0.2, 0.01, 0.2))             ## origin is at ceiling
ball = sphere(pos=vector(0.0,-0.25,0.0), radius=0.025, color=color.orange, make_trail=True) 
#ball = sphere(pos=vector(0.0,-0.35,0.0), radius=0.025, color=color.orange, make_trail=True)
spring = helix(pos=ceiling.pos, axis=ball.pos-ceiling.pos, color=color.cyan, thickness=.003, coils=40, radius=0.015) ## change the color to be your spring color


## constants and data
g = vector(0,-10.0,0)
ball.m = 1      
r0 = 0.25 
ks =100         
kv = 0.5          

## initial values
ball.v = vector(0,0,0)
Fgrav = ball.m*g
t = 0           
dt = .01  

## improve the display
scene.autoscale = True          
scene.center = vector(0,-r0,0)   
scene.waitfor('click')          

#graph
traj = gcurve(color=color.red)

## calculation loop

while t < 30:
    rate(100)
    # spring force
    r = mag(ball.pos)
    s = r - r0
    rhat = norm(ball.pos)
    Fspr = -ks*s*rhat
    
    #damping force
    #Fdamp = -kv*ball.v
    
    Fnet = Fgrav + Fspr #+ Fdamp

    # time stepping
    ball.v = ball.v + Fnet/ball.m*dt
    ball.pos = ball.pos + ball.v*dt
    spring.axis = ball.pos
    t = t + dt
    
    traj.plot(pos=(t,ball.pos.y))
