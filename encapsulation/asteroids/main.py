import arcade
import random

from asteroid import Asteroid
from ship import Ship

# Constant Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Game(arcade.Window):
    """
    This is where all of our game logic will go
    """

    def __init__(self, width, height):
        """
        Starting the game with 5 asteroids, setting backgound
        color, creating a ship, and inheriting the parent's init method
        """
        super().__init__(width, height)

        # Filling an array with 5 asteroids
        self.asteroids = []
        for asteroid in range(5):
            asteroid = Asteroid()
            self.asteroids.append(asteroid)

        # Bullets array to keep track of bullets
        self.bullets = []

        # Create a ship for our game
        self.ship = Ship()

        # A variable to let the ship know when to advance
        self.advance = False

        # These variablse let the ship know whether to rotate
        # or not
        self.rotate_left = False
        self.rotate_right = False

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.

        arcade.start_render()

        # Draws the player ship
        self.ship.draw()

        # Draw all asteroids in the asteroids array
        for asteroid in self.asteroids:
            asteroid.draw()

        # Draws all bullets, if any, in the array
        if len(self.bullets) > 0:
            for bullet in self.bullets:
                bullet.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # advances the ship
        self.ship.advance()

        # Checks to see if the ship is thrusting, or yeilding
        if self.advance:
            self.ship.thrust()
        else:
            self.ship.yeild()

        # Applies the correct rotation
        if self.rotate_left:
            self.ship.rotate(1)
        if self.rotate_right:
            self.ship.rotate(-1)

        # Makes sure the ship wraps around the screen
        self.ship.wrap()

        # call all update methods for the asteroids, if any
        if len(self.asteroids) > 0:
            for asteroid in self.asteroids:
                asteroid.advance()
                asteroid.rotate()
                asteroid.wrap()

        # Advances all bullets, if any, in the array
        if len(self.bullets) > 0:
            for bullet in self.bullets:
                bullet.advance()
                bullet.wrap()

                # Checks the bullet's lifespan and removes it if zero
                if not bullet.check_lifespan():
                    self.bullets.remove(bullet)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed. Mostly
        being used for handling ship movement.
        """

        # This will call the ship's Thrust method
        if key == arcade.key.UP:
            self.advance = True

        # Sets left ship rotation to true
        if key == arcade.key.LEFT:
            self.rotate_left = True

        # Sets right ship rotation to true
        if key == arcade.key.RIGHT:
            self.rotate_right = True

        # Checks to see if the ship wants to fire a bullet
        if key == arcade.key.SPACE:
            bullet = self.ship.shoot()

            # Appends the bullet to the bullets array
            self.bullets.append(bullet)

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. This function also handles
        ship movement.
        """

        # Stops using the Ship's thrust method, ship yeilds
        if key == arcade.key.UP:
            self.advance = False

        # Sets left ship rotation to false
        if key == arcade.key.LEFT:
            self.rotate_left = False

        # Sets right ship rotation to false
        if key == arcade.key.RIGHT:
            self.rotate_right = False


# Start the game
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
