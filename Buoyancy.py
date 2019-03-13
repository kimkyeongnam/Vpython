GlowScript 2.4 VPython
#####################부력!!!###########################
#object
water = box(size=vec(10,10,10), color = color.blue, opacity = 0.5)      #opacity=투명도, 1.0 불투명, 0.5 반투명, 1.5 완전불투명
wood = box(pos=vec(0,0,0), size=vec(1,1,1), texture = textures.wood)    #texture=무늬

# setting
wood.v = vec(0,0,0)     #초기속도
wood.rho = 950          #나무토막 밀도(kg/m**3)
water.rho = 1000        #물 밀도
wood.volume = wood.size.x*wood.size.y*wood.size.z
wood.volume_im = wood.volume    #부피
wood.m = wood.rho*wood.volume   #F=mg, 질량=밀도*부피
g = vec(0,-9.8,0)   #중력가속도
#부력=water.rho*wood.volume*-g
kv = 1000   #나무토막 떠오르는 속도 저항계수
kv_im = kv  #공기저항력은 물에 비하면 없는 것이나 마찬가지
t = 0
dt = 0.03
thold = 0.001

def collision(pBox,pbox, thold):    #물(큰박스)이랑 나무(작은박스)랑 밑에서 닿나요??, 범위.. 너무너무너무너무작으면 인정해주자
    colcheck = (pbox.pos.y - 0.5*pbox.size.y) - (pBox.pos.y - 0.5*pBox.size.y)  #pbox.pos.y=0   // 나무토막 밑이랑 물이랑 닿나요???
    if colcheck < thold:
        return True
    else:
        return False
        
#|____|
#|색칠|->wood.m*g(잠긴부피)
#부력은 wood.vloume_im*water.rho*-g

def calc_im(pBox,pbox, kv):         #위에서 서로 닿는가?
    floatcheck = (pbox.pos.y + 0.5*pbox.size.y) - (pBox.pos.y + 0.5*pBox.size.y)
    #print(floatcheck)
    if floatcheck > 0:
        pbox.volume_im = pbox.volume - floatcheck*pbox.size.x*pbox.size.z   #잠긴부피=기존부피-떠있는부피
    else:
        pbox.volume_im = pbox.volume

    if pbox.volume_im < 0:
        pbox.volume_im = 0  #잠긴부분은 없습니다
    kv_im = pbox.volume_im/pbox.volume*kv   #비율
    return pbox.volume_im, kv_im

while t < 100:
    rate(100)
    #collision
    if collision(water, wood, thold):
        print("colliding")
        break
    wood.volume_im, kv_im = calc_im(water, wood, kv):
    print(wood.volume_im)
    #force
    wood.f = wood.m*g #grvity
    wood.f = wood.f - kv_im*mag(wood.v)**2*norm(wood.v) #drag
    wood.f = wood.f - water.rho*wood.volume_im*g #buoyancy
    #time integration
    wood.v = wood.v + wood.f/wood.m*dt
    wood.pos = wood.pos + wood.v*dt
    
    #time update
    t = t + dt

    #camera
    #scene.center = water.pos+vec(0,0.5*water.size.y,0)
