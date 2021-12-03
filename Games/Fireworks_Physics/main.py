import pygame
from FireField import FireField

WIDTH = 1024
HEIGHT = 768
FPS = 60
GRAVITY = 9.81
ALPHA = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class App:
    def __init__(self):
        self.display = pygame.display
        self.screen = self.display.set_mode((WIDTH, HEIGHT))
        self.alpha_surface = pygame.Surface((WIDTH, HEIGHT))
        self.alpha_surface.set_alpha(ALPHA)
        self.clock = pygame.time.Clock()
        self.fireField = FireField(self)

    def run(self):
        running = True
        while running:
            self.screen.blit(self.alpha_surface, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    self.fireField.add_explosion(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 50)

            self.fireField.update()
            self.fireField.draw()

            self.display.flip()

            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.run()
