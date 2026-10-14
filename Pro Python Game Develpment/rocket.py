import pygame 
from pygame.locals import *
pygame.init()
WIDTH=1000
HEIGHT=600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
space=pygame.image.load("/Volumes/Data/Боби/Coding/Pro Python Game Develpment/Pro-Python-Game-Development-main/Pro Python Game Develpment/space.jpeg")
rocket=pygame.image.load('/Volumes/Data/Боби/Coding/Pro Python Game Develpment/Pro-Python-Game-Development-main/Pro Python Game Develpment/rocket.jpeg')
x=500
y=200
keys=[False, False, False, False]
while y<400:
    screen.blit(space, (0,0))
    screen.blit(rocket, (x,y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_DOWN:
                keys[1]=True
            elif event.key==K_LEFT:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        elif event.type==pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False
            elif event.key==K_DOWN:
                keys[1]=False
            elif event.key==K_LEFT:
                keys[2]=False
            elif event.key==K_RIGHT:
                keys[3]=False
    if keys[0]:
        if y>0:
            y=y-1
    elif keys[1]:
        if y<400:
            y=y+1
    elif keys[2]:
        if x>0:
            x=x-1
    elif keys[3]:
        if x<1000:
            x=x+1