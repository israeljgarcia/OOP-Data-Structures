"""
File: pong.py
Original Author: Br. Burton
Designed to be completed by others
This program implements a simplistic version of the
classic Pong arcade game.
"""
import arcade
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5


class Pong(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Ball
        Paddle
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class,
    but should not have to if you don't want to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0

        # These are used to see if the user is
        # holding down the arrow keys
        self.holding_left = False
        self.holding_right = False

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.ball.draw()
        self.paddle.draw()

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

        # Move the ball forward one element in time
        self.ball.advance()

        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for ball at important places
        self.check_miss()
        self.check_hit()
        self.check_bounce()

    def check_hit(self):
        """
        Checks to see if the ball has hit the paddle
        and if so, calls its bounce method.
        :return:
        """
        too_close_x = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_y = (PADDLE_HEIGHT / 2) + BALL_RADIUS

        if (abs(self.ball.center.x - self.paddle.center.x) < too_close_x and
            abs(self.ball.center.y - self.paddle.center.y) < too_close_y and
                self.ball.velocity.dx > 0):
            # we are too close and moving right, this is a hit!
            self.ball.bounce_horizontal()
            self.score += SCORE_HIT

    def check_miss(self):
        """
        Checks to see if the ball went past the paddle
        and if so, restarts it.
        """
        if self.ball.center.x > SCREEN_WIDTH:
            # We missed!
            self.score -= SCORE_MISS
            self.ball.restart()

    def check_bounce(self):
        """
        Checks to see if the ball has hit the borders
        of the screen and if so, calls its bounce methods.
        """
        if self.ball.center.x < 0 and self.ball.velocity.dx < 0:
            self.ball.bounce_horizontal()

        if self.ball.center.y < 0 and self.ball.velocity.dy < 0:
            self.ball.bounce_vertical()

        if self.ball.center.y > SCREEN_HEIGHT and self.ball.velocity.dy > 0:
            self.ball.bounce_vertical()

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.paddle.move_down()

        if self.holding_right:
            self.paddle.move_up()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = True

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = True

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = False

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = False


class Paddle:
    """
    Structure for a Paddle object in Pong game. The Paddle
    is used to prevent the ball from passing the right edge
    of the screen. It is a rectangle that can move up and down.

    Member Variables: center(Point)

    Methods: draw(), move_up(), move_down()
    """

    def __init__(self):
        """
        Sets the Paddle position using a Point object

        Return: none
        """
        self.center = Point(SCREEN_WIDTH - 10, SCREEN_HEIGHT / 2)

    def draw(self):
        """
        Draws a ractangle (the paddle) to the screen.

        Return: none
        """
        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.BLACK)

    def move_up(self):
        """
        Adds 5 to the y position of the paddle if the 
        paddle position y does not exceed the screen height

        Return: none 
        """
        if self.center.y + PADDLE_HEIGHT / 2 < SCREEN_HEIGHT:
            self.center.y += 5

    def move_down(self):
        """
        Subtracts 5 from the y position of the paddle
        if the paddle position y does not go below 0

        Return: none
        """
        if self.center.y - PADDLE_HEIGHT / 2 > 0:
            self.center.y -= 5


class Ball:
    """
    The ball class creates a ball with a velocity and position.
    The ball advances according to it's velocity. It also
    has the ability to bounce off the edges of the screen.
    The ball can restarted.

    Member Variables: center(Point), velocity(Velocity)

    Methods: draw(), advance(), bounce_horizontal(), bounce_vertical(), restart()
    """

    def __init__(self):
        """
        The center variable is set to 10 pixels plus the ball radius
        in the x position, and an random position between 10 plus 
        the ball radius and the screen height minus the ball radius
        minus 10 pixels in the y position. This is stored in a Point
        object.

        The velocity is a Velocity object with a random dx value and
        a random dy value between 2 - 4 (float).
        """
        self.center = Point(BALL_RADIUS + 10, random.randint(10 +
                                                             BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS - 10))
        self.velocity = Velocity(random.uniform(
            2, 4), random.uniform(2, 4))

    def draw(self):
        """
        Draws a circle with a position of center.x and center.y
        and a radius of BALL_RADIUS

        Return: none
        """
        arcade.draw_circle_filled(
            self.center.x, self.center.y, BALL_RADIUS, arcade.color.BLACK)

    def advance(self):
        """
        Adds velocity.dx and velocity.dy to self.x and self.y
        respectively.

        Return: none
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def bounce_horizontal(self):
        """
        Multiplies current velocity.dx by -1

        Return: none
        """
        self.velocity.dx *= -1

    def bounce_vertical(self):
        """
        Multiplies current velocity.dy by -1
        """
        self.velocity.dy *= -1

    def restart(self):
        """
        Resets the ball's position and velocity.

        Return: none
        """
        self.__init__()


class Point:
    """
    Sets the self.x and self.y variables to the passed in
    x and y arguments.

    Parameters: x(float), y(float)

    Return: none
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Velocity:
    """
    Sets the self.dx and self.dy variables to the passed in
    dx and dy arguments.

    Parameters: dx(float), dy(float)

    Return: none
    """

    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy


    # Creates the game and starts it
window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
