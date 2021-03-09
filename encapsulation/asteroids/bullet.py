import arcade
from flying_object import FlyingObject


class Bullet(FlyingObject):
    def __init__(self):
        """
        Sets up the bullet for when it is fired
        """
        super().__init__()

        # The bullet has a radius of 10
        self.radius = 10

        # This is how fast the bullet travels per pixel
        self.speed = 10

        # This is the lifespan of the bullet. It will only
        # live for 60 frames.
        self.frames = 60

    def draw(self):
        """
        Draws the bullet and decreases the lifespan(frames) by 1 each time it is drawn (per frame)
        """
        arcade.draw_circle_filled(
            self.center.x, self.center.y, self.radius, arcade.color.YELLOW)
        self.frames -= 1

    def advance(self):
        """
        Applies velocity to the bullet's position
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def check_lifespan(self):
        """
        Checks the lifespan(frames) of the bullet. If the frames
        are below zero, it will return false, otherwise returns 
        true.

        return: bool
        """
        if self.frames <= 0:
            return False
        else:
            return True
