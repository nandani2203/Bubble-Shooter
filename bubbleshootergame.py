from tkinter import Y
from turtle import back
import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((800,600))

#player
img = pygame.image.load("D:\program\shooter.png")
img = pygame.transform.scale(img, (50,50))
xaxis = 370
yaxis = 520
xc = 0
#background
background = pygame.image.load("background1.jpg")

#enemy
e1imgl = []
variable = "n"
#e1img = pygame.transform.scale(e1img, (50,50))
exl = []
eyl = []
exc = []
eyc = []
img10 = pygame.image.load('bubble.jpeg') 
img10 = pygame.transform.scale(img10, (60,60))
e1imgl.append(img10)
img11 = pygame.image.load('bubble.jpeg') 
img11 = pygame.transform.scale(img11, (60,60))
e1imgl.append(img11)
img12 = pygame.image.load('bubble.jpeg') 
img12 = pygame.transform.scale(img12, (60,60))
e1imgl.append(img12)
img13 = pygame.image.load('bubble.jpeg') 
img13 = pygame.transform.scale(img13, (60,60))
e1imgl.append(img13)
img14 = pygame.image.load('bubble.jpeg') 
img14 = pygame.transform.scale(img11, (60,60))
e1imgl.append(img14)
img15 = pygame.image.load('bubble.jpeg') 
img15 = pygame.transform.scale(img12, (60,60))
e1imgl.append(img15)

n = 6
#score
scorev = 0
font = pygame.font.Font('freesansbold.ttf', 24)
scx = 10
scy = 10
def score_show(x,y):
    score = font.render(f'you killed{scorev} a bubble', True, (255,255,255))
    screen.blit((score), (x,y))
#pratham
prat = pygame.image.load("lovelybubble.jpeg")
prat = pygame.transform.scale(prat, (60,60))
px = random.randint(0,720)
py = random.randint(10,150)
pxc = 0.5
pyc = 20
for i in range(n):
  #imge = pygame.image.load('superman.png') 
  #imge = pygame.transform.scale(imge, (50,50))
  #e1imgl.append(imge)
  #e1img = pygame.transform.scale(e1img, (50,50))
  exl.append(random.randint(0,720))
  eyl.append(random.randint(10,150))
  exc.append(0.5)
  eyc.append(20)


#bullet
bimg = pygame.image.load('bullet.png')
bimg = pygame.transform.scale(bimg, (30,30))
bxt = 390
by = 500
by2 = 500
bulletstate = "ready"
bullet2state = "ready"
score = 0

#over

overfont = pygame.font.Font('freesansbold.ttf', 32)
def youkilled():
    gameover = overfont.render("omg you just killed the loveliest bubble", True, (255,255,255))
    screen.blit((gameover),(10,250))
def player(x,y):
    screen.blit((img),(x,y))
def enemy(x,y,i):
    screen.blit((e1imgl[i]),(x,y))
def bullet(x,y):
    screen.blit((bimg), (x,y))
    global bulletstate
    bulletstate = "fire"
def prathamx(x,y):
    screen.blit((prat),(x,y))
 
def collision(x,y,z,a):
    c = ((x-z)**2) + ((y-a)**2) 
    dis = c**0.5
    if dis <= 30:
          return True
    else:
          return False





running = True
while running:
    screen.fill((0,0,0))
    screen.blit((background),(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                xc = -0.4
            if event.key == pygame.K_d:
                xc = 0.4
            if event.key == pygame.K_SPACE:
                if bulletstate == "ready":
                    bxt = xaxis
                    bullet(bxt,by)
                 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                xc = 0
            if event.key == pygame.K_b:
                xc = 0
        

    xaxis += xc   
    if xaxis <= 0:
        xaxis = 0
    if xaxis>= 736:
        xaxis = 736
    player(xaxis,yaxis)
    for i in range(n):
     exl[i] += exc[i]
     if exl[i] <= 0:
        exc[i] = 0.5
        eyl[i] +=eyc[i]
     if exl[i] >=720:
        exc[i] = -0.5
        eyl[i] += eyc[i]
        
       
     collide = collision(exl[i],eyl[i],bxt,by)
    
     if collide == True:
        by = 480
        #print("hit")
        bulletstate ="ready"
        scorev += 1
        #print(score)
        exl[i] = random.randint(0,720)
        eyl[i] = random.randint(10,150)
     collidep = collision(px,py,bxt,by)
     if collidep == True:
         screen.blit((img),(200,200))
         
       
     if collidep == True:
        px = 2000
        variable = "f"
        for j in range(n):
            exl[j] = 2000
        youkilled()
        
        break
     if collidep == True:
         youkilled()
       
     enemy(exl[i],eyl[i],i)
    collidep = collision(px,py,bxt,by)
    if collidep == True:
     print("true")
     
    
     #enemy(exl[i],eyl[i],i)
    if by <= 0: 
        by = 480
        bulletstate = "ready"
    px += pxc
    if px <= 0:
        pxc = 0.5
        py += pyc
    if px >=720:
        pxc = -0.5
        py += pyc
    if variable == "f":
        youkilled()
     
    
         
    prathamx(px,py)
    score_show(scx,scy)        
     
    
       



    if bulletstate =="fire":
        bullet(bxt,by)
        by -= 1
     
     
    
    pygame.display.update()