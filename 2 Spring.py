GlowScript 2.4 VPython

## objects
ceiling = box(pos=vector(0,0,0), opacity = 1,size = vector(0.2, 0.01, 0.2))             ## origin is at ceiling
ball = sphere(pos=vector(0.05,-0.25,0.5), radius=0.025, color=color.orange, make_trail=False) 
ball2= sphere(pos=vec(0,-0.5,0),radius=0.025 ,color=color.white, make_trail=False)
spring = helix(pos=ceiling.pos, axis=ball.pos-ceiling.pos, color=color.cyan, thickness=.003, coils=40, radius=0.015) ## change the color to be your spring color
spring2 = helix(pos=ball.pos, axis =ball2.pos-ball.pos, color=color.magenta, thickness=.003,coils=40,radius=0.015)

## constants and data
g = vector(0,-9.8,0)

ball.m = 5     
ball2.m = 1
r0 = 0.25 
r02 = 0.0025
ks = 100   
ks2 = 50  
kv = 0.5  
kv2 = 1   

## initial values
ball.v = vector(0,0,0)
ball2.v = vector(0,0,0)

Fgrav = ball.m*g
Fgrav2 = ball2.m*g

t = 0           
dt = .01  

## improve the display
scene.autoscale = True          
scene.center = vector(0,-r0,0)   
scene.waitfor('click')          

#graph
traj = gcurve(color=color.red)
traj2 = gcurve(color=color.blue)

## calculation loop

while t < 30:
    rate(100)
    
    # spring force
    r = mag(ball.pos)
    s = r - r0
    rhat = norm(ball.pos)
    
    #spring2 force
    r2 = mag(ball2.pos - ball.pos)
    s2 = r2 - r02
    rhat2 = norm(ball2.pos - ball.pos)
    
    Fspr = -ks * s * rhat
    Fspr2 = -ks2 * s2 * rhat2
    
    #damping force
    Fdamp = -kv * dot(ball.v, rhat) * rhat
    Fdamp2 = -kv2 * dot(ball2.v, rhat2) * rhat2
    
    Fnet = Fgrav + Fspr + Fdamp - Fspr2
    Fnet2 = Fgrav2 + Fspr2 + Fdamp2

    # time stepping
    ball.v = ball.v + Fnet/ball.m*dt
    ball.pos = ball.pos + ball.v*dt
    
    ball2.v = ball2.v + Fnet2/ball2.m*dt
    ball2.pos = ball2.pos + ball2.v*dt    
    
    spring.axis = ball.pos - ceiling.pos
    spring2.pos = ball.pos
    spring2.axis = ball2.pos - ball.pos
    
    t = t + dt
    
    traj.plot(pos=(t,ball.pos.y))
    traj2.plot(pos=(t,ball2.pos.y))
