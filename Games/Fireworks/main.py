import pygame
import math
import random

pygame.init()

WIDTH = 1024
HEIGHT = 768
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

particles = []


class FireParticle:
    def __init__(self, x=50.00, y=50.00, color=(255, 255, 255), speed=5, direction=0, timer=460):
        self.status = True
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.direction = direction
        self.timer = timer

    def draw(self):
        if self.timer >= 360:
            pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), 3)
        elif self.timer >= 240:
            pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), 2)
        elif self.timer >= 180:
            pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), 1)
        else:
           self.status = False
        self.timer -= 1

    def update(self):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)


running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(50):
                rand_Color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                rand_Speed = random.randint(1, 8)
                rand_Direction = random.random() * 6.28319
                particle = FireParticle(pygame.mouse.get_pos()[0],
                                        pygame.mouse.get_pos()[1],
                                        rand_Color,
                                        rand_Speed,
                                        rand_Direction)
                particles.append(particle)

    for particle in particles:
        particle.update()
        if (particle.x > WIDTH) or (particle.x < 0)\
                or (particle.y < 0) or (particle.y > HEIGHT)\
                or (particle.status is False):
            particles.remove(particle)

    for particle in particles:
        particle.draw()

    pygame.display.update()

    clock.tick(FPS)
