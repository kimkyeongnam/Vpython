GlowScript 2.4 VPython

#drawing obj.
Earth = sphere(pos=vec(0,0,0), radius=6.4e6, color=color.blue)
craft = sphere(pos=vec(-10*Earth.radius, 0,0), radius=1e6, color=color.yellow,
make_trail=True)
Moon = sphere(pos=vec(4e8, 0,0), radius=1.75e6)

#constants
G = 6.7e-11
Earth.m = 6e24
craft.m = 15e3
Moon.m = 7e22

#initial vel.
#craft.v = vec(0,3.273e3,0)
craft.v = vec(0,2e3,0) # initial vel without moon
#craft.v = vec(0,4e3,0) # hyperbolic
#craft.v = vec(0,3.5e3,0) # hyperbolic
#craft.v = vec(0,3.3e3,0)
#craft.v = vec(0,3.27e3,0) #critical pt.
#craft.v = vec(0,3.273e3,0) #loop

#time
t = 0
dt = 3000

#time integration
while t < 10*365*24*60*60:
 rate(500)
 ##Force
 r = craft.pos - Earth.pos
 rmag = mag(r)
 rhat = r/rmag
 Earth.f = -G*Earth.m*craft.m/rmag**2*rhat

 rmoon = craft.pos - Moon.pos
 rmoon_mag = mag(rmoon)
 rmoon_hat = rmoon/rmoon_mag
 Moon.f = -G*Moon.m*craft.m/rmoon_mag**2*rmoon_hat

 craft.f = Earth.f + Moon.f
 #print("Fnet = ", Fnet)

 #integration
 craft.v = craft.v + craft.f/craft.m*dt
 craft.pos = craft.pos + craft.v*dt
 t = t+dt
