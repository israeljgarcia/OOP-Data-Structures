import random
import arcade
import math

from flying_object import FlyingObject

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Asteroid(FlyingObject):
    def __init__(self):
        super().__init__()
        self.speed = 1.5
        self.radius = 35
        self.angle = random.randint(1, 359)

        self.center.x = random.randint(100, SCREEN_WIDTH - 100)
        self.center.y = random.randint(100, SCREEN_HEIGHT - 100)

        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed

    def draw(self):
        img = "images/meteorGrey_big1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(
            x, y, width, height, texture, angle, alpha)

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def rotate(self):
        self.angle += 1

    def hit(self):
        pass
