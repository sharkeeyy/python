import pygame
from FireField import FireField

pygame.init()

WIDTH = 1024
HEIGHT = 768
FPS = 60
GRAVITY = 9.81
ALPHA = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.fireField = FireField(self)

    def run(self):
        running = True
        while running:
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    self.fireField.add_explosion(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 50)

            self.fireField.update()
            self.fireField.draw()

            pygame.display.flip()

            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.run()
