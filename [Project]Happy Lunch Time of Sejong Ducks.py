GlowScript 2.5 VPython

##Project: 세종오리들의 해피런치타임( Happy Lunch Time of Sejong Ducks)


####################################필드 만들기#################################
sky = box(pos=vec(0,0,0), size=vec(1000,1000,1000), color=color.white)  #큰 박스 = 하늘
sky_under = box(pos=vec(0,-70,0), size=vec(1000,0.3,1000))  #박스랑 물 y길이 차이가 커서 넣은 것. 확대해보면 이해할 수 있을거야
water_gameplay = box(pos = vec(0,0,0), size = vec(250,140,125), color = color.cyan, opacity = 0.3)
ground_right = box(pos=vec(135,69.7,0), size=vec(20,0.3,150), color=color.green)
ground_left = box(pos=vec(-135,69.7,0), size=vec(20,0.3,150), color=color.green)
ground_up = box(pos=vec(0,69.7,-70), size=vec(290,0.3,20), color=color.green)
ground_down = box(pos=vec(0,69.7,70), size=vec(290,0.3,20), color=color.green)
 
 
 
 
#####################################기본 정보##################################
scene.title = "<세종오리들의 해피 런치타임>     4조作 "
scene.center = vec(0,0,0)
scene.forward = -vec(0,200,700)
scene.range = 150
 
#오리 코드
duck_mouse = cone(pos = vec(0,0,0), axis = vec(-4,0,0), radius = 1, color = color.red)
duck_head = sphere(pos = vec(0,0,0), radius=2.5, color = color.yellow)
duck_body = ellipsoid(pos = vec(2.5,-4,0), length = 7.5, height = 5, width = 5, color = color.yellow)
duck_eye_left = sphere(pos = vec(-1,0.5,2), radius = 0.5, color = color.black)
duck_eye_right = sphere(pos = vec(-1,0.5,-2), radius = 0.5, color = color.black)
duck = compound([duck_mouse, duck_head, duck_body, duck_eye_left, duck_eye_right])
 
 
 
duck.pos = vec(0,70,0)
duck.v = vec(0,0,0) #초기속도
duck.rho = 0.3 #오리의 밀도
water_gameplay.rho = 1 #물의 밀도
duck.volume = duck.size.x*duck.size.y*duck.size.z #오리의 부피
duck.volume_im = duck.volume #오리가 잠겨있는 부피
duck.m = duck.rho*duck.volume #질량=밀도*부피
 
g = vec(0,-0.98,0) #중력
kv = 100 #유체저항력
kv_im = kv #물 표면에서 움직일때 저항력 -> 나중에 코딩!!
t = 0
dt = 0.05
thold = 0.001 #간격 보정용
dthrust = vec(0,0,0) #추진력
 
life = 5 #생명
score = 0 #점수
mylabel = label(pos = vec(170,110,0)) #점수판
 
#def reset(button):
    #btn_Start.disabled = False
    #duck.pos = vec(0,70,0)
 
 
 
####물고기
#(물고기의 기본형)
#fish_body =ellipsoid(pos = vec(0,0,0), length = 10, height=5, width = 3)
#fish_eyes = sphere(pos = vec(-3,1,2), radius = 0.5, color=color.black)
#fish_tail = cone(pos=vector(8,0,0), axis=vector(-5,0,0), radius=3)
#fish=compound([fish_body, fish_tail, fish_eyes])
 
#오른쪽에서 왼쪽으로 가는 물고기
rbodyList=[]
reyesList=[]
rtailList=[]
robjList=[]
 
for i in range(0,5):
    rbodyList.append(ellipsoid(pos = vec(0,0,0), length = 10, height=5, width = 3, color = vec(random(),random(),random())))
for i in range(0,5):
    reyesList.append(sphere(pos = vec(-3,1,2), radius = 0.5, color=color.black))
for i in range(0,5):
    rtailList.append(cone(pos=vec(8,0,0), axis=vec(-5,0,0), radius=3, color = vec(random(),random(),random())))
for i in range(0,5):
    robjList.append(compound([rbodyList[i], rtailList[i], reyesList[i]]))
    
for i in range(0,5):
    robjList[i].pos=vec(125,70-125*random(),0)
    robjList[i].v=(-1)*vec(random(),0,0)
    #속도가 너무 느린 물고기를 방지하기 위한 코드
    if robjList[i].v.x > -0.2:
        robjList[i].v = robjList[i].v + vec(-0.5,0,0)
    robjList[i].v= robjList[i].v*10
 
#왼쪽에서 오른쪽으로 가는 물고기
lbodyList=[]
leyesList=[]
ltailList=[]
lobjList=[]
 
for i in range(0,5):
    lbodyList.append(ellipsoid(pos = vec(0,0,0), length = 10, height=5, width = 3, color = vec(random(),random(),random())))
for i in range(0,5):
    leyesList.append(sphere(pos = vec(-3,1,-2), radius = 0.5, color=color.black))
for i in range(0,5):
    ltailList.append(cone(pos=vector(8,0,0), axis=vector(-5,0,0), radius=3, color = vec(random(),random(),random())))
for i in range(0,5):
    lobjList.append(compound([lbodyList[i], ltailList[i], leyesList[i]]))
    
for i in range(0,5):
    lobjList[i].pos=vec(-125,70-125*random(),0)
    lobjList[i].rotate(angle=pi, axis=vec(0,1,0))
    lobjList[i].v=vec(random(),0,0)
    #속도가 너무 느린 물고기를 방지하기 위한 코드
    if lobjList[i].v.x < 0.2:
        lobjList[i].v = lobjList[i].v + vec(0.5,0,0)
    lobjList[i].v= lobjList[i].v*10
 
rcntlist=[]
lcntlist=[]
for i in range(0,5):
    rcntlist.append(0)
for i in range(0,5):
    lcntlist.append(0)
def fish():
    for i in range(0,5):
        robjList[i].pos = robjList[i].pos + robjList[i].v*dt
        lobjList[i].pos = lobjList[i].pos + lobjList[i].v*dt
        
        #if i>0 and i<5:
            #if robjList[i-1].pos.y - robjList[i].pos.y < 10:
            #    robjList[i].pos.y = robjList[i].pos.y - 25
            #if lobjList[i-1].pos.y - lobjList[i].pos.y < 10:
            #    lobjList[i].pos.y = lobjList[i].pos.y - 25    
            
            #물고기가 수조 끝에 닿을때
            
        if robjList[i].pos.x<-120:
            rcntlist[i]=0  # 요 코드는 무슨 의미 ?
            robjList[i].pos=vec(125,70-125*random(),0)
            robjList[i].visible = True
                
        if lobjList[i].pos.x>120:
            lcntlist[i]=0
            lobjList[i].pos=vec(-125,70-125*random(),0)
            lobjList[i].visible = True
                
        if robjList[i].pos.y <= -70 or robjList[i].pos.y>70:
            robjList[i].visible = False #높이가 70 위로 올라가거나 -70 밑으로 내려가면 유저가 닿지 못하는곳이니 안보이게 처리
        if lobjList[i].pos.y <= -70 or lobjList[i].pos.y>70:
            lobjList[i].visible = False #높이가 70 위로 올라가거나 -70 밑으로 내려가면 유저가 닿지 못하는곳이니 안보이게 처리
 
 
 
 
#공기방울
#edge = sphere(pos = vec(0,0,0), color = color.white, radius = 3, opacity =  0.5)
#pong = sphere(pos = vec(0,0,0), color = color.cyan, radius = 2.8)
#point = sphere(pos = vec(-1,1,1.3), color = color.white, radius = 1)
 
 
 
 
 
############################필드 벗어나지 못하게 만들기#########################
 
 
 
 
 
 
 
######################################키 조작###################################
cnt=0
 
#duck_position_judge = []
 
def keydown(evt):
    global s
    s = evt.key
    if s == 'left':
        #duck_position_judge.append(-2)
        #if cnt == 0:
        global dthrust
        dthrust=vec(-1000,0,0)
            #cnt += 1
        #else:
            #if duck_position_judge[cnt-1] == 2:
            #global dthrust
            #dthrust=vec(-15000,0,0)
                #duck = duck.rotate(angle=pi, axis=vec(0,1,0))
                #cnt += 1
        
    if s == 'right':
        #duck_position_define.judge(2)
        #if cnt == 0:
        global dthrust
        dthrust=vec(1000,0,0)
            #duck = duck.rotate(angle=pi, axis=vec(0,1,0))
            #cnt += 1
        #else:
            #if duck_position_judge[cnt-1] == -2:
                #global dthrust
                #dthrust=vec(15000,0,0)
                #duck = duck.rotate(angle=pi, axis=vec(0,1,0))
                #cnt += 1
                            
        
    if s == 'up':
        global dthrust
        dthrust=vec(0,1000,0)
        
    if s == 'down':
        global dthrust
        dthrust=vec(0,-900,0)
 
 
 
def keyup(evt):
    global s
    s = evt.key
    if s == 'left':
        global dthrust
        dthrust=vec(0,0,0)
        
    if s == 'right':
        global dthrust
        dthrust=vec(0,0,0)
        
    if s == 'up':
        global dthrust
        dthrust=vec(0,0,0)
        
    if s == 'down':
        global dthrust
        dthrust=vec(0,0,0)
        
        
scene.bind('keydown', keydown)
scene.bind('keyup', keyup)
 
 
 
 
 
#####################################재  생#####################################
judge = 0
time=0
error=0
while(1):
    rate(80)
    #점수 표시(점수판)
    mylabel.text = 'life : ' + life + '\n' + 'score : ' + score  
    
    #게임 종료 조건
    if life==0:
        mylabel.text='GAME OVER'
        break;
        
    #오리 힘 조절하기
    if(duck.pos.y>65 and duck.pos.y<=70):
        duck.f = duck.m*g
        duck.f = duck.f - kv_im*mag(duck.v)**2*norm(duck.v) #물의 저항력. 속도**2에 반대방향으로.
        duck.f = duck.f - water_gameplay.rho*duck.volume_im*g #부력=물 밀도*나무 부피*-g 앞에 -니까 -g를 곱한셈.
        duck.f = duck.f + dthrust
    else:
        duck.f=duck.m*g
        duck.f = duck.f + dthrust
    #print duck.f
    #물고기 움직임
    for i in range(0,5):
        
        if -10<robjList[i].pos.x-duck.pos.x<10 and -10<robjList[i].pos.y-duck.pos.y<10:
            robjList[i].visible = False
            rcntlist[i]=rcntlist[i]+1
            if rcntlist[i]==1:
                score += 10
                
        if -10<lobjList[i].pos.x-duck.pos.x<10 and -10<lobjList[i].pos.y-duck.pos.y<10:
            lobjList[i].visible = False
            lcntlist[i]+=1
            if lcntlist[i]==1:
                score += 10
 
    #time integration
    k=duck.v.x
    
    duck.v = duck.v + duck.f/duck.m*dt
    
    #오리 방향
    if k==0:
        #if error==0:
        if duck.v.x>0:
            duck.rotate(angle=pi, axis=vec(0,1,0))
                
        #else if duck.v.x<0:
    else if k*duck.v.x < 0:
        duck.rotate(angle=pi, axis=vec(0,1,0))
    duck.pos = duck.pos + duck.v*dt
 
    fish()
 
   
    
    #필드 벗어남: life -= 1
    if duck.pos.y>=70+15:
        duck.pos=vec(0,70,0)
        life=life-1
        if duck.v.x>0:
            duck.rotate(angle=pi, axis=vec(0,1,0))
        #    error=1
            
        
        dthrust=vec(0,0,0)
        duck.v=vec(0,0,0)
    else if duck.pos.x<=-(125+5):
        duck.pos=vec(0,70,0)
        life=life-1
        if duck.v.x>0:
            duck.rotate(angle=pi, axis=vec(0,1,0))
            #error=1
        dthrust=vec(0,0,0)
        duck.v=vec(0,0,0)
    else if duck.pos.x>=125+5:
        duck.pos=vec(0,70,0)
        life=life-1
        if duck.v.x>0:
            duck.rotate(angle=pi, axis=vec(0,1,0))
            #error=1
        dthrust=vec(0,0,0)
        duck.v=vec(0,0,0)
    else if duck.pos.y<=-(70+5):
        duck.pos=vec(0,70,0)
        life=life-1
        if duck.v.x>0:
            duck.rotate(angle=pi, axis=vec(0,1,0))
            #error=1
        dthrust=vec(0,0,0)
        duck.v=vec(0,0,0)
 
    #time update
    t = t + dt
