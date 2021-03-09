from point import Point
from velocity import Velocity

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class FlyingObject:
    """
    The flying object class is a partent to all objects that
    will be floating through space for the Asteroids game.
    It has basic attributes and methods for these classes.
    """

    def __init__(self):
        """
        Initializes all essential variables for a flying object.
        """
        self.center = Point()
        self.velocity = Velocity()
        self.speed = 0
        self.radius = 0
        self.angle = 90

    def draw(self):
        """
        This method is used to draw the object onto the game screen
        """
        pass

    def advance(self):
        """
        This method is used to advance the object forward
        """
        pass

    def rotate(self):
        """
        This method adds/subtracts degrees to the object's orientation
        """
        pass

    def wrap(self):
        """
        Checks to see if an object passed a boundry. If the object
        passed a boundry, then the object's position will be set to
        the opposite side of the screen. This makes it look like the 
        objects are wrapping around the screen when floating through
        space.
        """

        # Checking to see if the object image is off the left side
        # of the screen
        if self.center.x + self.radius + 5 < 0:
            self.center.x = (SCREEN_WIDTH + self.radius - 1)

        # Checking right side
        if self.center.x - self.radius - 5 > SCREEN_WIDTH:
            self.center.x = (0 - self.radius)

        # Checking bottom side
        if self.center.y + self.radius + 5 < 0:
            self.center.y = (SCREEN_HEIGHT + self.radius + 1)

        # Checking top
        if self.center.y - self.radius - 5 > SCREEN_HEIGHT:
            self.center.y = (0 - self.radius - 1)
