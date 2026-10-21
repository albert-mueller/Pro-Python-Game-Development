import pygame
pygame.init()
WIDTH=500
HEIGHT=500
space_background=pygame.image.load("space.jpeg")
spaceship_yellow=pygame.image.load("spaceship_yellow.png")
spaceship_red=pygame.image.load("spaceship_red.png")
screen=pygame.display.set_mode((WIDTH, HEIGHT))

def yellow_spaceship(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT]:
        yellow.x=yellow.x-1
    elif keys_pressed[pygame.K_RIGHT]:
        yellow.x=yellow.x+1
    elif keys_pressed[pygame.K_UP]:
        yellow.y=yellow.y-1
    elif keys_pressed[pygame.K_DOWN]:
        yellow.y=yellow.y+1

def red_spaceship(keys_pressed, red):
    if keys_pressed[pygame.K_a]:
        red.x=red.x-1
    elif keys_pressed[pygame.K_d]:
        red.x=red.x+1
    elif keys_pressed[pygame.K_w]:
        red.y=red.y-1
    elif keys_pressed[pygame.K_s]:
        red.y=red.y+1

def display_on_screen():
    screen.blit(space_background, (0,0))
    screen.blit(spaceship_yellow, (250, 250))
    screen.blit(spaceship_red, (500, 500))
    pygame.display.update()
red=pygame.Rect(9,9, 55, 40)
yellow=pygame.Rect(500,500, 55, 40)
while True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
    display_on_screen()
    keys_pressed=pygame.key.get_pressed()
    red_spaceship(keys_pressed, red)
    yellow_spaceship(keys_pressed, yellow)
