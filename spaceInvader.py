import pygame
import random
import math
from pygame import mixer
#intialize the pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("Space invader")

#background
background=pygame.image.load('D:/tkinter gui/pyGame/9.png')
background=pygame.transform.scale(background,(800,600))

#player
playerimg=pygame.image.load('D:/tkinter gui/pyGame/player.png')
playerimg=pygame.transform.scale(playerimg,(64,64))
playerX=370
playerY=480
playerX_change=0

#enemy
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

enemy=pygame.image.load('D:/tkinter gui/pyGame/download.png')
enemy=pygame.transform.scale(enemy,(64,64))

for i in range(num_of_enemies):

    enemyimg.append(enemy)
    enemyX.append(random.randint(0,734))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.4)
    enemyY_change.append(30)

#bullet 
bulletimg=pygame.image.load('D:/tkinter gui/pyGame/bullet.png')
bulletimg=pygame.transform.scale(bulletimg,(32,32))
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=0.7
bullet_state="ready" #ready state is u cant see bullet on screen

#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

#game over text
over_font=pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))

def player(x,y):
    screen.blit(playerimg,(x,y)) #to draw on screen
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(((enemyX-bulletX)**2)+((enemyY-bulletY)**2))
    if distance<27:
        return True
    else:
        return False

#game loop
running=True
while running:
    #filling background
    screen.fill((0,0,0)) #RGB values to be filled
    #background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        #if key stroke is pressed check R/L
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                #left
                playerX_change=-0.3
            if event.key==pygame.K_RIGHT:
                #right
                playerX_change=0.3
            if event.key==pygame.K_SPACE and bullet_state=="ready":
                bullet_sound=mixer.Sound('D:/tkinter gui/pyGame/laser.wav')
                bullet_sound.play()
                bulletX=playerX
                fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                #key is released
                playerX_change=0



    
    #checking boundaries
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    
    #enemy movement
    for i in range(num_of_enemies):

        #game over
        if enemyY[i]>430:
            for j in range(num_of_enemies):
                enemyY[j]=2000

            game_over_text()
            break
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=0.4
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-0.4
            enemyY[i]+=enemyY_change[i]

        #collision
        collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound=mixer.Sound('D:/tkinter gui/pyGame/explosion.wav')
            explosion_sound.play()
            bulletY=480
            bullet_state="ready"
            score_value+=1
            
            enemyX[i]=random.randint(0,734)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)

    #bullet movement
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    
    

    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()