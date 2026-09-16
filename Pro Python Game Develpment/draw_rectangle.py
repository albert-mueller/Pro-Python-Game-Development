import pygame
screen=pygame.display.set_mode((600,600))
pygame.init()
class Rectangle:
    def __init__(self, color, x, y, w, h):
        self.color=color
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.screen=screen
    def draw_rectangle(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
    def grow_rectangle(self, grow):
        self.w+=grow
        self.h+=grow
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
rectangle=Rectangle("blue", 78, 100, 100, 400)
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            rectangle.draw_rectangle()
            pygame.display.update()
        elif i.type==pygame.MOUSEBUTTONUP:
            rectangle.grow_rectangle(10)
            pygame.display.update()