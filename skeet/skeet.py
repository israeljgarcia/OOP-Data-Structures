"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others

This program implements an awesome version of skeet.
"""
import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """

    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, 360-self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.background = None

        self.bullets = []

        # TODO: Create a list for your targets (similar to the above bullets)
        self.targets = []

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """
        Set up the background.
        """
        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        self.background = arcade.load_texture('background.png')

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        # TODO: iterate through your targets and draw them...
        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance
        for target in self.targets:
            target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # TODO: Decide what type of target to create and append it to the list
        target_type = random.randint(1, 3)
        if target_type == 1:
            target = StandardTarget()
            self.targets.append(target)
        elif target_type == 2:
            target = StrongTarget()
            self.targets.append(target)
        elif target_type == 3:
            target = SafeTarget()
            self.targets.append(target)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                            abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.

        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


class FlyingObject:
    """
    This class is a base class for objects that fly across the screen.
    A flying object has a Point, Velocity, radius, and is alive boolean.

    Member Variables: center(Point), velocity(Velocity), radius(float), alive(bool)

    Methods: __init__(), advance(), is_off_screen(screen_width: float, screen_height: float)
    """

    def __init__(self):
        """
        Initializes center to a Point, velocity to a Velocity,
        radius to 0.0, and alive to true.

        return: none
        """
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.alive = True

    def advance(self):
        """
        Applies velocity to the position of the object by adding
        dx to x and dy to y.

        return: none
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def is_off_screen(self, screen_width, screen_height):
        """
        Checks to see if the object is outside of the given parameters.
        If the object is outside, then alive is set to false and the object
        will be destroyed.

        return: none
        """
        if self.center.x > screen_width or self.center.x < 0 or self.center.y > screen_height or self.center.y < 0:
            self.alive = False


class Bullet(FlyingObject):
    """
    The bullet class is used to create bullets that can destroy
    targets. The bullets can advance, check if they are off screen,
    and fire. 

    Member Variables: (See FlyingObject class)

    Methods: (See FlyingObject class), draw(), fire(angle) 
    """

    def __init__(self):
        """
        See FlyingObject class
        """
        super().__init__()

    def advance(self):
        """
        See FlyingObject class
        """
        super().advance()

    def draw(self):
        """
        Draws a bullet on the screen at the position 0,0.

        Return: none
        """
        self.radius = BULLET_RADIUS
        arcade.draw_circle_filled(
            self.center.x, self.center.y, self.radius, BULLET_COLOR)

    def is_off_screen(self, screen_width, screen_height):
        """
        See FlyingObject class
        """
        super().is_off_screen(screen_width, screen_height)

    def fire(self, angle):
        """
        Calls the draw method to draw a bullet on the screen
        then applies velocity to the bullet at the angle the 
        mouse is pointing.

        Return: none
        """
        sound = arcade.Sound('pew.wav')
        sound.play()
        self.draw()

        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED


class Target(FlyingObject):
    """
    The target class is used to create a target on the screen
    with the Arcade library. The target can advance, get hit,
    and check to see if it is off screen. 

    Member Variables: Flying bject variables (See FlyingObject class), lives(int)

    Methods: (FlyingObject methods), hit()
    """

    def __init__(self):
        """
        Sets a random x and y position for the target's
        on-screen position. Sets x velocity to random between
        1 and 5. Sets y velocity to random between -2 and 5.

        return: none
        """
        super().__init__()  # See FlyingObject class

        # Randomizing target spawn point
        self.center.x = random.randint(0, SCREEN_WIDTH / 2)
        self.center.y = random.randint(SCREEN_HEIGHT / 2, SCREEN_HEIGHT)

        # Randomizing velocity
        self.velocity.dx = random.randint(1, 5)
        self.velocity.dy = random.randint(-2, 5)

    def advance(self):
        """
        See FlyingObject class
        """
        super().advance()

    def draw(self):
        """
        Draws an outline of a circle at a position that was 
        dertermined on __init__(). The circle has the number of lives
        inside of the outline. 

        return: none
        """
        self.radius = 10
        arcade.draw_circle_filled(
            self.center.x, self.center.y, self.radius, TARGET_COLOR)

    def is_off_screen(self, screen_width, screen_height):
        """
        See FlyingObject class
        """
        super().is_off_screen(screen_width, screen_height)

    def hit(self):
        """
        Subtracts 1 life from the target and returns 1 for the 
        game score. The target will die if lives reach 0 or below.

        return: 1
        """
        sound = arcade.Sound('hit.wav')
        sound.play()


class StandardTarget(Target):
    """
    A Standard target is the easiest target to hit and destroy.
    Very similar to a Target, but different functionality for
    hit function.

    Member Variables: (See Target class)

    Member Functions: (See Target class), hit()
    """

    def __init__(self):
        super().__init__()

    def hit(self):
        super().hit()
        self.alive = False
        return 1


class StrongTarget(Target):
    """
    The strong target takes 3 hits to destroy and awards 5 points upon 
    being destroyed. Has a slower velocity than other targets

    Member Variables: (See Target class), lives(int)

    Methods: (See Target class), __init__(), draw(), hit()
    """

    def __init__(self):
        """
        Sets random velocity for dx and dy and sets lives to 3
        """
        super().__init__()
        self.velocity.dx = random.randint(1, 3)
        self.velocity.dy = random.randint(-2, 3)
        self.lives = 3

    def draw(self):
        """
        Draws an outlines circle with the number of lives inside
        as text.
        """
        self.radius = 10

        # drawing the circle
        arcade.draw_circle_outline(
            self.center.x, self.center.y, self.radius, TARGET_COLOR)

        # adding the text inside the circle
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y,
                         TARGET_COLOR, font_size=10)

    def hit(self):
        """
        Updates lives remaining and returns 1 point
        it hit. Returns 5 when destroyed.

        return: 1 or 5
        """
        super().hit()
        self.lives -= 1
        if self.lives <= 0:
            self.alive = False
            return 5
        return 1


class SafeTarget(Target):
    """
    A safe target should not be hit and will penalize the 
    player if it is hit. 10 points will be deducted.
    """

    def __init__(self):
        super().__init__()

    def draw(self):
        """
        Draws a filled rectangle. Radius is actually the square's sides size here
        because radius is used for bullet collision.

        return: none
        """
        self.radius = 13
        arcade.draw_rectangle_filled(self.center.x, self.center.y,
                                     self.radius, self.radius, arcade.color.RED)

    def hit(self):
        """
        Destroyed when hit (sets alive to False) and decucts 10 points from score

        return: -10
        """
        super().hit()
        self.alive = False
        return -10


class Point:
    """
    A point is represented by two varaibales: x and y to
    determine the position of the point on a screen.

    Member Variables: x(float), y(float)

    Methods: __init__()
    """

    def __init__(self):
        """
        Sets the self.x and self.y variables to 0

        Return: none
        """
        self.x = 0
        self.y = 0


class Velocity:
    """
    Velocity is represented by two variables: dx and dy.
    dx is speed in the x direction and dy is speed in the 
    y direction. This is useful in the update method of the
    Arcade library.

    Member Variables: dx(float), dy(float)
    """

    def __init__(self):
        """
        Sets the self.dx and self.dy variables to 0

        Return: none
        """
        self.dx = 0
        self.dy = 0


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
window.setup()
arcade.run()
