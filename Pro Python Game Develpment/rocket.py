import pygame 
from pygame.locals import *
pygame.init()
WIDTH=1000
HEIGHT=400
screen=pygame.display.set_mode((WIDTH, HEIGHT))
space=pygame.image.load("/Users/boyan1/Downloads/Pro Python Game Develpment/space.jpeg")
rocket=pygame.image.load('/Users/boyan1/Downloads/Pro Python Game Develpment/rocket.jpeg')
x=500
y=200
while y<400:
    screen.blit(space, (0,0))
    screen.blit(rocket, (x,y))
    pygame.display.update()
