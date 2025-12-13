import pygame
import math
WIDHT, HEIGHT = 800,600
G=9.8

class object:
    def __init__(self,x,y,r,color,mass):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.mass = mass
        self.vel_x = 0
        self.vel_y = 0
    def update(self):
        self.x+=self.vel_x
        self.y+=self.vel_y
    def pyshics(self,times,framerate):
        self.h=HEIGHT - self.y - self.r
        if self.h<0:
            self.y=HEIGHT - self.r
        else:
            self.vel_y+=G*(times/1000)*(1/framerate)
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(int(self.x),int(self.y)),self.r)
pygame.init()
screen = pygame.display.set_mode((WIDHT,HEIGHT))
clock = pygame.time.Clock()
ball = object(400,50,20,(255,255,255),1)
framerate=120
running=True
while running:
    times=pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    ball.pyshics(times,framerate)
    ball.update()
    screen.fill((0,0,0))
    ball.draw(screen)
    pygame.display.flip()
    clock.tick(framerate)
pygame.quit()
