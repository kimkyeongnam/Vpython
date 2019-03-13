GlowScript 2.4 VPython

scene.range = 20
ground = box(pos=vector(0,-10.05,0), size=vector(40, .1,1), color=color.white)
spaceship = box(pos=vector(0,8,0), size=vector(2,5,2), color=color.yellow)
spaceship.m = 1
spaceship.v = vector (0 ,0 ,0)

g=1/6 * vector(0,-10,0)

t = 0
dt = 0.05
scale =5.0
FgravArrow = arrow(pos=spaceship.pos, axis=scale*spaceship.m*g, color=color.red)
Fthrust = vector(0,0,0)
FthrustArrow = arrow(pos=spaceship.pos, axis=Fthrust, color= color.cyan)

def keydown(evt):
    s = evt.key
    if s == 'left':
        global Fthrust
        Fthrust=vector(-4,0,0)
    if s == 'right':
        global Fthrust
        Fthrust=vector(4,0,0)

def keyup(evt):
    s = evt.key
    if s == 'left':
        global Fthrust
        Fthrust=vector(0,0,0)
    if s == 'right':
        global Fthrust
        Fthrust=vector(0,0,0)
        
def up(ev):
    global Fthrust
    Fthrust=vector(0,0,0)

def down(ev):
    global Fthrust
    Fthrust=vector(0,4,0)

scene.bind('mouseup', up)
scene.bind('mousedown', down)
scene.bind('keydown', keydown)
scene.bind('keyup', keyup)

while t < 1000:
    rate(100)
    Fgrav = spaceship.m * g
    Fnet = Fgrav + Fthrust
    print(Fthrust)
    
    spaceship.v = spaceship.v + Fnet/spaceship.m*dt
    spaceship.pos = spaceship.pos + spaceship.v*dt
    #collision
    if (spaceship.pos.y - spaceship.height/2 < ground.pos.y +
        ground.height/2):
        print("spaceship has landed")
        break
    t = t + dt
    FgravArrow.pos = spaceship.pos
    FgravArrow.axis= scale*Fgrav
    FthrustArrow.pos = spaceship.pos
    FthrustArrow.axis= scale*Fthrust
