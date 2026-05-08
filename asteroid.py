import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            new1 = self.velocity.rotate(random_angle)
            new2 = self.velocity.rotate(random_angle * -1)
            newA1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            newA1.velocity = new1 * 1.2
            newA2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            newA2.velocity = new2 * 1.2

    