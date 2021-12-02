import pygame
import math
import random

FPS = 60
GRAVITY = 9.81
WIDTH = 1024
HEIGHT = 768


class FireParticle:
    def __init__(self, x0, y0, app):
        self.screen = app.screen
        self.isAlive = True
        self.frame = 0
        self.x = 0
        self.y = 0
        self.x0 = x0
        self.y0 = y0
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed = random.randint(2000, 5000) * 0.01
        self.direction = random.random() * 2 * math.pi

    def draw(self):
        if self.frame <= 200:
            pygame.draw.circle(self.screen, self.color, (round(self.x), round(self.y)), 3)
        elif self.frame <= 320:
            pygame.draw.circle(self.screen, self.color, (round(self.x), round(self.y)), 2)
        elif self.frame <= 460:
            pygame.draw.circle(self.screen, self.color, (round(self.x), round(self.y)), 1)
        else:
            pass
        self.frame += 1

    def update(self):
        self.x = self.x0 + self.speed * math.cos(self.direction) * self.frame / FPS
        self.y = self.y0 - self.speed * math.sin(self.direction) * self.frame / FPS + \
                  (GRAVITY * math.pow(self.frame / FPS, 2)) / 2
        if (self.x > WIDTH) or (self.x < 0) or (self.y < 0) or (self.y > HEIGHT):
            self.isAlive = False
        if self.frame > 460:
            self.isAlive = False
