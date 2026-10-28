import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
class Apple:
    def __init__(self, color, pos, radius):
        self.color=color
        self.pos=pos
        self.radius=radius
        self.screen=screen
    def draw_circle(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)
    def grow_circle(self, draw):
        self.radius+=draw
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)
circle_obj=Apple("blue", (200,10), 30)
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            circle_obj.draw_circle()
            pygame.display.update()
        elif i.type==pygame.MOUSEBUTTONUP:
            circle_obj.grow_circle(10)
            pygame.display.update()