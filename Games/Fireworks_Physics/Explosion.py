from FireParticle import FireParticle


class Explosion:
    def __init__(self, x, y, app, particles_count=50):
        self.app = app
        self.isAlive = True
        self.x = x
        self.y = y
        self.particles_count = particles_count
        self.particles = []
        for i in range(self.particles_count):
            self.particles.append(FireParticle(x, y, app))

    def update(self):
        for particle in self.particles:
            particle.update()
            if not particle.isAlive:
                self.particles.remove(particle)
            if len(self.particles) == 0:
                self.isAlive = False

    def draw(self):
        for particle in self.particles:
            particle.draw()
