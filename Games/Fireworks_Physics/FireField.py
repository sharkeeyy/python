from Explosion import Explosion


class FireField:
    def __init__(self, app):
        self.app = app
        self.explosions = []

    def add_explosion(self, start_x, start_y, particles_count):
        self.explosions.append(Explosion(start_x, start_y, self.app, particles_count))

    def update(self):
        for explosion in self.explosions:
            explosion.update()
            if not explosion.isAlive:
                self.explosions.remove(explosion)

    def draw(self):
        for explosion in self.explosions:
            explosion.draw()
