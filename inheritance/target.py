from flyingobject import FlyingObject

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


class Target(FlyingObject):
    def __init__(self):
        super().__init__()
        self.center.x = random.randint(0, SCREEN_WIDTH / 2)
        self.center.y = random.randint(SCREEN_HEIGHT / 2, SCREEN_HEIGHT)
        self.velocity.dx = 1
        self.lives = 1

    def advance(self):
        super().advance()

    def draw(self):
        self.radius = TARGET_RADIUS
        arcade.draw_circle_outline(
            self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y,
                         TARGET_COLOR, font_size=20)

    def is_off_screen(self, screen_width, screen_height):
        super().is_off_screen(screen_width, screen_height)

    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            self.alive = False
        return 1
