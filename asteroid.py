import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        baby_one_vector = self.velocity.rotate(angle)
        baby_two_vector = self.velocity.rotate(-angle)
        baby_radius = self.radius - ASTEROID_MIN_RADIUS
        baby_one = Asteroid(self.position[0], self.position[1], baby_radius)
        baby_two = Asteroid(self.position[0], self.position[1], baby_radius)
        baby_one.velocity = baby_one_vector * 1.2
        baby_two.velocity = baby_two_vector * 1.2