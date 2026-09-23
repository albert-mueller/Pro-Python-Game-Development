import pygame
import time
WIDTH=400
HEIGHT=400
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
bmw=pygame.image.load("car.jpeg")
bmw=pygame.transform.scale(bmw, (WIDTH, HEIGHT))
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    font=pygame.font.SysFont("Calibri", 20)
    text=font.render("BMW", True, "yellow")
    screen.blit(bmw, (0,0))
    screen.blit(text, (200,200))
    pygame.display.update()
    time.sleep(3)
    ferrari=pygame.image.load("car2.jpeg")
    ferrari=pygame.transform.scale(ferrari, (WIDTH, HEIGHT))
    screen.blit(ferrari, (0,0))
    pygame.display.update()
    time.sleep(3)
    macbookpro=pygame.image.load("macbookpro.jpg")
    macbookpro=pygame.transform.scale(macbookpro, (WIDTH, HEIGHT))
    screen.blit(macbookpro, (0,0))
    pygame.display.update()
    time.sleep(3)
