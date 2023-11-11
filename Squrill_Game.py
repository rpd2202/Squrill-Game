import pygame,sys,random,math
from pygame.locals import *
from pygame import mixer
pygame.init()
d=pygame.display.set_mode((500,400))
pygame.display.set_caption("Squirrel Game")
mixer.music.load('tetrisc.wav')
mixer.music.play(-1)
pygame.display.set_icon(pygame.image.load('squirrel.png'))
x=455
y=200
Y_C=0
n_x=40
n_y=random.choice((30,70,115,155,200,240,285,320))
score=0
left=5
def to_gameover():
    global n_y,n_x,left
    if n_x>450:
        tof=1
    else:
        tof=0
    if tof==1:
        left-=1
        n_x=40
        n_y=random.choice((30,70,115,155,200,240,285,325))
def gameover():
    global left,x,y
    if left<=0:
        d.blit(pygame.transform.scale(pygame.image.load('flippyboard.png'),(500,400)),(0,0))
        __f=pygame.font.Font('freesansbold.ttf',30)
        __ren=__f.render("Game Over!",True,(0,0,0))
        d.blit(__ren,(170,130))
        af=pygame.font.Font('freesansbold.ttf',25)
        sa=af.render("Your Score :"+str(score),True,(0,0,0))
        d.blit(sa,(170,180))
        x=0
        y=0
def collision():
    global n_y,n_x,x,y,score
    dis=math.sqrt(math.pow(n_x-x,2)+math.pow(n_y-y,2))
    if dis<35:
        torf=True
    else:
        torf=False
    if torf==True:
        
        score+=1
        n_x=40
        n_y=random.choice((30,70,115,155,200,240,285,325))
def dis_score():
    global left
    f=pygame.font.Font('freesansbold.ttf',25)
    sc=f.render("Score :"+str(score),True,(255,0,0))
    d.blit(sc,(10,5))
    ff=pygame.font.Font('freesansbold.ttf',12)
    d.blit(ff.render("How to play:",True,(255,255,0)),(10,345+5))
    d.blit(ff.render("use arrow keys or wasd to move",True,(255,255,0)),(10,355+5))
    d.blit(ff.render("w or a to move up",True,(255,255,0)),(10,365+5))
    d.blit(ff.render("s or d to move down",True,(255,255,0)),(10,375+5))
    fa=pygame.font.Font('freesansbold.ttf',20)
    d.blit(fa.render("You have "+str(left)+" chances",True,(128,0,128)),(300,7))#only use +(concatination)
    aa=pygame.font.Font('freesansbold.ttf',15)
    d.blit(aa.render("Creater:Team GladiQ",True,(255,255,255)),(340,380))
def dif_sqspeed():
    global score,Y_C
    if score>=0 and score<5:
        Y_C=1*5
    if score>=5 and score<10:
        Y_C=1.5*5
    if score>=10 and score<15:
        Y_C=2.0*5
    if score>=15 and score<20:
        Y_C=2.5*5
    if score>=20 and score<25:
        Y_C=3.0*5
    if score>=25 and score<30:
        Y_C=3.5*5
    if score>=30 and score<35:
        Y_C=4.0*5
    if score>=35 and score<40:
        Y_C=4.5*5
    if score>=40 and score<45:
        Y_C=5.0*5
    if score>=45 and score<50:
        Y_C=5.5*5
    if score>=50:
        Y_C=6.0*5
    return Y_C
def to_exit():
    if i.type==QUIT:
        pygame.quit()
        sys.exit()
def to_move():
    global X_C,Y_C,score
    if i.type==pygame.KEYDOWN:
        if i.key==pygame.K_LEFT:
            Y_C=-dif_sqspeed()
            sound=mixer.Sound('match0.wav')
            sound.play()
        if i.key==pygame.K_w:
            Y_C=-dif_sqspeed()
            sound=mixer.Sound('match0.wav')
            sound.play()
        if i.key==pygame.K_a:
            Y_C=-dif_sqspeed()
            sound=mixer.Sound('match0.wav')
            sound.play()
        if i.key==pygame.K_s:
            Y_C=dif_sqspeed()
            sound=mixer.Sound('match0.wav')
            sound.play()
        if i.key==pygame.K_d:
            Y_C=dif_sqspeed()
            sound=mixer.Sound('match0.wav')
            sound.play()
        if i.key==pygame.K_RIGHT:
            Y_C=dif_sqspeed()
            sound=mixer.Sound('match0.wav')
            sound.play()
        if i.key==pygame.K_UP:
            Y_C=-dif_sqspeed()
            sound=mixer.Sound('match0.wav')
            sound.play()
        if i.key==pygame.K_DOWN:
            Y_C=dif_sqspeed()
            sound=mixer.Sound('match0.wav')
            sound.play()
    if i.type==pygame.KEYUP:
        if i.key==pygame.K_UP or i.key==pygame.K_w or i.key==pygame.K_DOWN or i.key==pygame.K_s or i.key==pygame.K_LEFT or i.key==pygame.K_a or i.key==pygame.K_RIGHT or i.key==pygame.K_d:
            Y_C=0 
def to_stopbeyondlimit():
    global x,y,n_x
    if y<=18:
        y=18
    if y>=315:
        y=315
    if n_x>=450:
        n_x=450
def placeimage():
    global x,y,n_x,n_y
    d.blit(pygame.transform.scale(pygame.image.load('back.png'),(500,400)),(0,0))
    d.blit(pygame.transform.scale(pygame.image.load('squirrel.png'),(32,32)),(x,y))
    d.blit(pygame.transform.scale(pygame.image.load('nut.png'),(25,25)),(n_x,n_y))        
    __x=0
    __y=30
    for i in range(0,4):
            d.blit(pygame.image.load('Tree_Tall.png'),(__x,__y))
            __y+=85
    __a=0
    __b=345
    for i in range(0,10):
        d.blit(pygame.image.load('b.png'),(__a,__b))
        __a+=50
def difficulty():
    global score,dif
    if score>=0 and score<5:
        dif=1.0
    if score>=5 and score<10:
        dif=1.5
    if score>=10 and score<15:
        dif=2.0
    if score>=15 and score<20:
        dif=2.5
    if score>=20 and score<25:
        dif=3.0
    if score>=25 and score<30:
        dif=3.5
    if score>=30 and score<35:
        dif=4.0
    if score>=35 and score<40:
        dif=4.5
    if score>=40 and score<45:
        dif=5.0
    if score>=45 and score<50:
        dif=5.5
    if score>=50:
        dif=6.0
    return dif
while True:
    to_stopbeyondlimit() 
    n_x+=difficulty()
    for i in pygame.event.get():
        to_exit()
        y+=Y_C
        to_move()
    placeimage()    
    collision()
    dis_score()
    to_gameover()
    gameover()
    pygame.display.update()
