import pygame
import sys

pygame.init()

WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Battle")

# Load images (make sure paths match your local files)
space_background = pygame.image.load("/Volumes/Data/Боби/Coding/Pro Python Game Develpment/space.jpeg")
spaceship_yellow = pygame.image.load("/Volumes/Data/Боби/Coding/Pro Python Game Develpment/spaceship_yellow.png")
spaceship_red = pygame.image.load("/Volumes/Data/Боби/Coding/Pro Python Game Develpment/spaceship_red.png")

size_img_red = pygame.transform.rotate(pygame.transform.scale(spaceship_red, (100, 100)), 270)
size_img_yellow = pygame.transform.rotate(pygame.transform.scale(spaceship_yellow, (100, 100)), 90)

# Define rect positions and sizes
red = pygame.Rect(500, 300, 55, 40)
yellow = pygame.Rect(100, 300, 55, 40)
rectangle=pygame.Rect(345,0,10,700)
VEL = 5  # Movement speed

def yellow_spaceship(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x-VEL>0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x+VEL+yellow.width<rectangle.x-40:
        yellow.x += VEL
    if keys_pressed[pygame.K_UP] and yellow.y-VEL>0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN] and yellow.y+VEL+yellow.height<HEIGHT-15:
        yellow.y += VEL

def red_spaceship(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x-VEL>rectangle.x+rectangle.width:
        red.x -= VEL
    if keys_pressed[pygame.K_d] and red.x+VEL+red.width<WIDTH-40:
        red.x += VEL
    if keys_pressed[pygame.K_w] and red.y-VEL>0:
        red.y -= VEL
    if keys_pressed[pygame.K_s] and red.y+VEL+red.height<HEIGHT-15:
        red.y += VEL

def display_on_screen():
    screen.blit(space_background, (0, 0))
    # Use the Rect coordinates instead of hardcoded numbers
    screen.blit(size_img_yellow, (yellow.x, yellow.y))
    screen.blit(size_img_red, (red.x, red.y))
    pygame.draw.rect(screen,"blue",rectangle)
    pygame.display.update()

clock = pygame.time.Clock()
FPS = 60

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys_pressed = pygame.key.get_pressed()
    red_spaceship(keys_pressed, red)
    yellow_spaceship(keys_pressed, yellow)
    display_on_screen()