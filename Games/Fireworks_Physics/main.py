import pygame
import math
import random

pygame.init()

WIDTH = 1024
HEIGHT = 768
FPS = 60
GRAVITY = 9.81

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

particles = []


class FireParticle:
    def __init__(self, x0=50.00, y0=50.00, color=(255, 255, 255), speed=5, direction=0):
        self.status = True
        self.frame = 0
        self.x = 0
        self.y = 0
        self.x0 = x0
        self.y0 = y0
        self.color = color
        self.speed = speed
        self.direction = direction

    def draw(self):
        if self.frame <= 200:
            pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), 3)
        elif self.frame <= 320:
            pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), 2)
        elif self.frame <= 460:
            pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), 1)
        else:
            self.status = False
        self.frame += 1

    def update(self):
        self.x = self.x0 + self.speed * math.cos(self.direction) * self.frame / FPS
        self.y = self.y0 - self.speed * math.sin(self.direction) * self.frame / FPS + \
                  (GRAVITY * math.pow(self.frame / FPS, 2)) / 2


running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(50):
                rand_Color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                rand_Speed = random.randint(2000, 5000) * 0.01
                rand_Direction = random.random() * 6.28319
                particle = FireParticle(pygame.mouse.get_pos()[0],
                                        pygame.mouse.get_pos()[1],
                                        rand_Color,
                                        rand_Speed,
                                        rand_Direction)
                particles.append(particle)

    for particle in particles:
        particle.update()
        if (particle.x > WIDTH) or (particle.x < 0) \
                or (particle.y < 0) or (particle.y > HEIGHT) \
                or (particle.status is False):
            particles.remove(particle)

    for particle in particles:
        particle.draw()

    pygame.display.update()

    clock.tick(FPS)
