import pygame

import sys

pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("Blaze")

#image info
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
#FPS

clock=pygame.time.Clock()

# GAME VARIALBE

swidth=500
sheight=480

x = 50
y= 400
width=64
height=64

vel=5

left =False
right=False
walkcount=0


isjump=False
jumpCount=10

v_y=100
G=10

t=10

run =True

def redraw():
    global walkcount
    win.blit(bg,(0,0))
    if walkcount+1>=27:
        walkcount=0
    if left:
        win.blit(walkLeft[walkcount//3],(x,y))
        walkcount+=1
    elif right:
        win.blit(walkRight[walkcount//3],(x,y))
        walkcount+=1
    else:
        win.blit(char,(x,y))
        walkcount=0            
    pygame.display.update() 

# main loop
while run:
    clock.tick(27)
    
  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-=vel
        if x<0:
            x=0
        left=True
        right=False

    elif keys[pygame.K_RIGHT]:
        x+=vel
        if x+width>swidth:
            x=swidth-width
        left=False
        right=True    
    else:
        right=False
        left=False
        walkcount=0
    if not(isjump): 
        '''       
        if keys[pygame.K_UP]:
            y-=vel
            if y<0:
                y=0
        if keys[pygame.K_DOWN]:
            y+=vel
            if y+height>sheight:
                y=sheight-height
        '''    
        if keys[pygame.K_SPACE]:
            isjump=True
            right=False
            left=False
            walkcount=0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isjump = False


    redraw()





pygame.quit()