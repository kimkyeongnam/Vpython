GlowScript 2.4 VPython

riList = []
objList = []
scene.range=5

ground = box(length = 10, height = 0.001, width = 10) 

for i in range(0,100):
    riList.append(vec(0,0,0))
for ri in riList:
    objList.append(sphere(pos = ri, radius = 0.05, color = vec(random(), random(), random()),
    make_trail=True, retain = 50))

vi = vec(0,5.0,0)
a = vec(0,-3.0,0)

for obj in objList:
    obj.v = vi #+ vector(random(),random(),random())

t = 0
dt = 0.01
i=0

def explosion(evt):
    print("exploding!")
    for obj in objList:
        i+=1
        if i%2!=0:
            obj.v = obj.v + vec(random()-0.5,random()-0.5,random()-0.5)
        else:
            obj.v = obj.v - vec(random()-0.5,random()-0.5,random()-0.5)

scene.bind('click', explosion)

while t < 15:
    rate(100)   
    for obj in objList:
        obj.v = obj.v + a*dt
        obj.pos = obj.pos + obj.v*dt
        if obj.pos.y < 0:
            obj.pos.y = 0
            obj.color =  vec(random(), random(), random())
            obj.v.y = -0.8*obj.v.y
    t = t + dt
