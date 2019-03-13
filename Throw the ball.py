GlowScript 2.4 VPython
#함수
#
InitPos = vec(10,0,0)
def startBtn(b): 
    ball.make_trail = True
    b.disabled = True
    btn_Start.disalbed = True
    return b.disabled

def reset(b):
    btn_Start.disabled = False
    ball.make_trail = False
    ball.pos = InitPos
    
def gravitySlider(s):
    return s.value
def angleSlider(s):
    return s.value
    
#파라미터
radius_ = 0.035
dragCoeffieicnt = 0.35
thick = 1.
L = 250.
#scene
scene.center = vector(0.45*L,0,0)
scene.forward = -vector(-L/4.,L/4.,L) 

#버튼
btn_Start = button(text = 'start',bind = startBtn)
reset = button(text = 'restart',bind = reset)
scene.append_to_caption('\n\n')

#슬라이더
gravity = slider(bind = gravitySlider, min = 0, max = 20,step = 0.1)
gravity.value = 9.8
scene.append_to_caption('  gravity\n\n')

angle = slider(bind = angleSlider, min = 0, max = 90, step = 1)
angle.value = 15
scene.append_to_caption('  angle\n\n')


theta0 = angle.value * 2/pi/360
v0 = 100.*1600./3600.
#오브젝트
floor = box(pos = vector(L/2.,-thick/2.,0), size = vector(2*L,thick,L/4.), color=color.green)
ball = sphere(pos = InitPos, radius = 20.*radius_, color = color.white, make_trail = True)
ball.m = 0.155
mylabel = label(pos = vec(10,100,0))
#장애물
obs1 = ring(pos = vector(150,30,0),axis = vector(0,1,0),radius =5, thickness = 1)
obs1.velocity = vector(-.3,0,0)

#각도 포인터 
arr = arrow(pos = ball.pos, axis = vec(v0*cos(angle.value),v0*sin(angle.value),0),shaftwidth = 1)
dt = 0.01

time=0
fr = 30

while 1 :    
    rate(300)
    if ball.pos.y>=0:
        mylabel.text = 'gravity : ' + gravity.value + '\n' + 'angle : ' + angle.value        
        Fgrav = vec(0,-ball.m * gravity.value,0)
        theta0 = angle.value * 2. * pi / 360.
        arr.axis = vec(v0*cos(theta0),v0*sin(theta0),0)
        
        F=Fgrav
        
        if btn_Start.disabled:            
            ball.p = ball.p + F * dt
            ball.pos = ball.pos + (ball.p/ball.m) * dt
        else:
            ball.p = ball.m * vector(v0*cos(theta0),v0*sin(theta0),0)
         
    obs1.pos = obs1.pos + obs1.velocity
    time = time+dt
    if -120 > obs1.pos.x or obs1.pos.x > 350:
        obs1.velocity = -obs1.velocity
