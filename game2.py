import pygame
import sys
pygame.init()
pygame.mixer.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("Blaze")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()
 
score=0

bulletsound=pygame.mixer.Sound('bullet.wav')
hitsound=pygame.mixer.Sound('hit.wav')
music=pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

class player(object):
   # global score
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox=(self.x+18,self.y+10,30,55)
        self.health=1200

    def draw(self, win):
        pygame.draw.rect(win, (0,123,123), (self.x+5,self.y-6, self.health//20,10))
        if self.health<1200:
            pygame.draw.rect(win, (255,0,0), (self.x+5+self.health//20,self.y-6, (1200-self.health)//20,10))
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                #print('vdf')
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            elif self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))                
        self.hitbox=(self.x+18,self.y+10,30,55)
        #pygame.draw.rect(win, (0,0,255), self.hitbox,1)
    def hit(self):
        global score
        self.health-=10
        if self.health<=0:
            pygame.quit()
        font1=pygame.font.SysFont('comicsanas', 100, bold=False, italic=False)
        tex=font1.render('-10',1,(255,0,0))
        win.blit(tex,(190,200))
        #score-=10
        pygame.display.update()
        i=0
        while i<2:
            pygame.display.update()
            pygame.time.delay(50)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=101
                    pygame.quit()
        print("HIT BY GOBLIN")
        score-=10
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y

        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

# ENEMIES
class enemy():
    #global score
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.vel=3
        self.walkCount=0
        self.path=[x,end]
        self.hitbox=(self.x+18,self.y+2,30,55)
        self.health=900
        self.defeat=False
    def draw(self,win):
        self.move()
        
        if not(self.defeat):
            pygame.draw.rect(win, (0,123,123), (self.x+5,self.y-6, self.health//14,10))
            if self.health<900:
                pygame.draw.rect(win, (255,0,0), (self.x+self.health//14+5,self.y-6, (900-self.health)//14,10))
            if self.walkCount>=33:
                self.walkCount=0  
            #print(self.vel)  
            if self.vel>0:
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1    
            else:
                #print('madarchod')
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            self.hitbox=(self.x+18,self.y+2,30,55)
            #pygame.draw.rect(win, (0,0,255), self.hitbox,1)
    def move(self):
        if self.vel>0:
            if self.x+self.vel<self.end:
                self.x+=self.vel
            else:
                self.vel*=-1
                self.x+=self.vel
                self.walkCount=0
        else :
            if self.x+self.vel>self.path[0]:
                self.x+=self.vel
            else:                
                self.vel*=-1
                self.x+=self.vel
                self.walkCount=0
    def hit(self):
        #global score
        #score+=1
        self.health-=10
        if self.health>0:
            self.defeat=False
        else:
            self.defeat=True
        
        print("HIT")            


def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    rest=font.render("SCORE: "+str(score),1,(0,0,0))
    win.blit(rest,(350,10))
    sensei.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()


#mainloop
man = player(200, 410, 64,64)
bullets = []
font=pygame.font.SysFont('comicsans', 30, bold=True, italic=False)
sensei=enemy(0,410,64,64,410)
run = True
shootloop=0
hitcount=0
while run:
    clock.tick(27)
    if shootloop>0:
        shootloop+=1
    if shootloop>3:
        shootloop=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets:
        if bullet.y-bullet.radius<sensei.hitbox[1]+sensei.hitbox[3] and bullet.y+bullet.radius>sensei.hitbox[1]:
            if bullet.x+bullet.radius>sensei.hitbox[0] and bullet.x-bullet.radius<sensei.hitbox[0]+sensei.hitbox[2]:
                #score-=10
                sensei.hit()
                hitsound.play()
                score+=10
                bullets.pop(bullets.index(bullet))    
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop==0:
        bulletsound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 9:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
        shootloop=1
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    print(hitcount)        
    if ((man.hitbox[0]>sensei.hitbox[0] and man.hitbox[0]<sensei.hitbox[0]+sensei.hitbox[2]) or (man.hitbox[0]+man.hitbox[2]>sensei.hitbox[0] and man.hitbox[0]+man.hitbox[2]<sensei.hitbox[0]+sensei.hitbox[2])) :
        if (man.hitbox[1]>sensei.hitbox[1] and man.hitbox[1]<sensei.hitbox[1]+sensei.hitbox[3]) or (man.hitbox[1]+man.hitbox[3]<sensei.hitbox[1]+sensei.hitbox[3] and man.hitbox[1]+man.hitbox[3]>sensei.hitbox[1]):
            if hitcount==0:
                man.hit()
                hitcount=1
            
                
    else:
        hitcount=0
    redrawGameWindow()

pygame.quit()