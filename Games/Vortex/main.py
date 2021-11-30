import pygame as pg
import random
import math

RES = WIDTH, HEIGHT = 1600, 900
NUM_STARS = 1500


vec2, vec3 = pg.math.Vector2, pg.math.Vector3
CENTER = vec2(WIDTH // 2, HEIGHT // 2)
COLORS = 'red green blue purple orange cyan'.split()
Z_DISTANCE = 40
ALPHA = 100


class Star:
    def __init__(self, app):
        self.screen = app.screen
        self.pos3d = self.get_pos3d()
        self.velocity = random.uniform(0.05, 0.25)
        self.color = random.choice(COLORS)
        self.screen_pos = vec2(0, 0)
        self.size = 10

    def get_pos3d(self, scale_pos=35):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.randrange(HEIGHT // scale_pos, HEIGHT) * scale_pos
        x = radius * math.sin(angle)
        y = radius * math.cos(angle)
        return vec3(x, y, Z_DISTANCE)

    def update(self):
        self.pos3d.z -= self.velocity
        if self.pos3d.z < 1:
            self.pos3d = self.get_pos3d()
        self.screen_pos = vec2(self.pos3d.x, self.pos3d.y) / self.pos3d.z + CENTER
        self.size = (Z_DISTANCE - self.pos3d.z) / (0.2 * self.pos3d.z)

    def draw(self):
        pg.draw.rect(self.screen, self.color, (*self.screen_pos, self.size, self.size))


class Starfield:
    def __init__(self, app):
        self.stars = []
        for i in range(NUM_STARS):
            self.stars.append(Star(app))

    def update(self):
        for star in self.stars:
            star.update()
        self.stars.sort(key=lambda star: star.pos3d.z, reverse=True)
        for star in self.stars:
            star.draw()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)
        self.alpha_surface = pg.Surface(RES)
        self.alpha_surface.set_alpha(ALPHA)
        self.clock = pg.time.Clock()
        self.starfield = Starfield(self)

    def run(self):
        while True:
            # self.screen.fill('black')
            self.screen.blit(self.alpha_surface, (0, 0))

            self.starfield.update()

            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
