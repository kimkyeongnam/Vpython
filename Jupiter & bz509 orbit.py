GlowScript 2.4 VPython

scale_factor_sun = 30.0
scale_factor_jupiter = 300.0
scale_factor_bz509 =10000.0
#creating sun
sun = sphere(pos=vector(0,0,0),radius=scale_factor_sun*695700000,color=color.yellow,
make_trail = True) #m
sun.mass = 1.989e30 #kg
sun.v = vec(0,0,0) #m/s
r0 = 778500000000 # distance between sun and jupiter unit:m
G = 6.67e-11 #unit: N*m^2/kg^2
#creating jupiter
jupiter = sphere(pos=vector(-r0,0,0),radius=scale_factor_jupiter*69911000, make_trail =
True)# m
#jupiter.mass = 1.898e27 #kg
jupiter.mass = 1.898e29 #kg
jupiter.v = vec(0,-13054,0) #m/s
#jupiter.v = vec(0,0,0) #m/s
#creating BZ509
bz509 = sphere(pos=vector(0.98*r0,0,0), radius=scale_factor_bz509*911000,
make_trail = True, color=color.green)# m
bz509.mass = 1e2 #kg
bz509.v = vec(-6070,-12070,000) #m/s
#time
t = 0
dt = 60000
while t < 120*365*24*60*60:
 rate(500)
 # calc. force
 jupiter.force = -G*jupiter.mass*sun.mass/mag(sun.pos-jupiter.pos)**2*norm(jupiter.pos)
 bz509.force = -G*bz509.mass*sun.mass/mag(sun.pos-bz509.pos)**2*norm(bz509.pos)
 bz509.force_j = -G*bz509.mass*jupiter.mass/mag(jupiter.pos-bz509.pos)**2*norm(bz509.pos-jupiter.pos)
 #sun.force = -jupiter.force - bz509.force
 #bz509.force_j = vec(0,0,0)
 #vel. update
 jupiter.v = jupiter.v + jupiter.force/jupiter.mass*dt
 bz509.v = bz509.v + (bz509.force+bz509.force_j)/bz509.mass*dt
 #sun.v = sun.v + sun.force/sun.mass*dt
 #pos. update
 jupiter.pos = jupiter.pos + jupiter.v*dt
 bz509.pos = bz509.pos + bz509.v*dt
 #sun.pos = sun.pos + sun.v*dt
 t = t + dt
