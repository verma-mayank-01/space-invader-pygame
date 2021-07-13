import pygame
import random

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Dice Simulator")

def load(image):
    face=pygame.image.load(image)
    face=pygame.transform.scale(face,(400,300))
    screen.blit(face,(100,100))

run=True
while run:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    if event.type==pygame.KEYDOWN:
        count=random.randint(1,6)
        print(count)
        if event.key==pygame.K_RETURN:
            
            '''if(count==1):
                image='D:/tkinter gui/pyGame/1.png'
                load(image)
            if count==2:
                image='D:/tkinter gui/pyGame/2.png'
                load(image)
            if count==3:
                image='D:/tkinter gui/pyGame/3.png'
                load(image)
            if count==4:
                image='D:/tkinter gui/pyGame/4.png'
                load(image)
            if count==5:
                image='D:/tkinter gui/pyGame/5.png'
                load(image)
            if count==6:
                image='D:/tkinter gui/pyGame/6.png'
                load(image)'''
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_RETURN:
            if(count==1):
                image='D:/tkinter gui/pyGame/1.png'
                load(image)
            if count==2:
                image='D:/tkinter gui/pyGame/2.png'
                load(image)
            if count==3:
                image='D:/tkinter gui/pyGame/3.png'
                load(image)
            if count==4:
                image='D:/tkinter gui/pyGame/4.png'
                load(image)
            if count==5:
                image='D:/tkinter gui/pyGame/5.png'
                load(image)
            if count==6:
                image='D:/tkinter gui/pyGame/6.png'
                load(image)
        



    pygame.display.update() 


