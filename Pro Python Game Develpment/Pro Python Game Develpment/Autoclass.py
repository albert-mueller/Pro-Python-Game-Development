import pgzrun
import random
WIDTH=800
HEIGHT=400
class Ball:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.vx=200
        self.vy=0
        self.size=30
    def circle(self):
        pos=(self.x, self.y)
        screen.draw.filled_circle(pos, self.size, "blue")
ball=Ball(100,100)
def draw():
    screen.clear()
    ball.circle()
def update(dt):
    uy=ball.vy
    ball.vy+=2000.0*dt
    ball.y+=(uy+ball.vy)*0.5*dt
    if ball.y>HEIGHT-ball.size:
        ball.y=HEIGHT-ball.size
        ball.vy=-ball.vy*0.9
    ball.x+=ball.vx*dt
    if ball.x>WIDTH-ball.size or ball.x<ball.size:
        ball.vx = -ball.vx
def on_key_down(key):
    if key==keys.S:
        ball.vy=-500
pgzrun.go()