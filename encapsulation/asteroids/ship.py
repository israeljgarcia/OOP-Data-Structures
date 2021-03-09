import random
import math
import arcade

from flying_object import FlyingObject
from bullet import Bullet

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ship(FlyingObject):
    def __init__(self):
        """
        Set up the ship to be placed in the center of the screen
        """
        super().__init__()

        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2

        self.radius = 30

        self.speed = .25

    def draw(self):
        """
        Draw the ship in the middle of the screen
        """
        img = "images/playerShip1_orange.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle - 90

        arcade.draw_texture_rectangle(
            x, y, width, height, texture, angle, alpha)

    def rotate(self, direction):
        """
        Rotate the ship at 3 degrees per second
        """
        self.angle += 3 * direction

    def shoot(self):
        """
        Instantiates a bullet and sets it to be drawn in frot of the ship
        when fired.

        Local Variables: bullet(Bullet)

        return: bullet(Bullet)
        """
        # Instantiates a bullet
        bullet = Bullet()
        bullet.center.x = self.center.x + \
            math.cos(math.radians(self.angle)) * 10
        bullet.center.y = self.center.y + \
            math.sin(math.radians(self.angle)) * 10
        bullet.angle = self.angle

        bullet.velocity.dx = math.cos(math.radians(self.angle)) * bullet.speed
        bullet.velocity.dy = math.sin(math.radians(self.angle)) * bullet.speed

        return bullet

    def advance(self):
        """
        Velocity is applied to the position of the ship

        return: none
        """
        # Calculate the velocity for dx and dy
        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed

        # Apply the velocity to the object's center
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

        # Caps the speed at 10 pixels per frame
        if self.speed > 10:
            self.speed = 10

    def thrust(self):
        """
        Increases speed by .25 per frame
        """
        self.speed += .25

    def yeild(self):
        """
        Slows how the ship by .25 per frame if speed is above 0
        """
        if self.speed > 0:
            self.speed -= .25
