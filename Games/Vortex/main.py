import pygame as pg
import random
import math

RES = WIDTH, HEIGHT = 1024, 768
NUM_STARS = 100


vec2, vec3 = pg.math.Vector2, pg.math.Vector3
CENTER = vec2(HEIGHT // 2, WIDTH // 2)
COLORS = 'red green blue purple orange cyan'.split()
Z_DISTANCE = 40


class Star:
    def __init__(self, app):
        self.screen = app.screen
        self.pos3d = self.get_pos3d()
        self.velocity = random.uniform(0.05, 0.25)

    def get_pos3d(self):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.randrange(HEIGHT)
        x = radius * math.sin(angle)
        y = radius * math.cos(angle)
        return vec3(x, y, Z_DISTANCE)

    def update(self):
        pass

    def draw(self):
        pass


class Starfield:
    def __init__(self, app):
        self.stars = []
        for i in range(NUM_STARS):
            self.stars.append(Star(app))

    def update(self):
        for star in self.stars:
            star.update()
            star.draw()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.starfield = Starfield(self)

    def run(self):
        while True:
            self.screen.fill('black')

            self.starfield.update()

            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
