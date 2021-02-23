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


class Bullet(FlyingObject):
    def __init__(self):
        super().__init__()

    def advance(self):
        super().advance()

    def draw(self):
        self.radius = BULLET_RADIUS
        arcade.draw_circle_filled(
            self.center.x, self.center.y, self.radius, BULLET_COLOR)

    def is_off_screen(self, screen_width, screen_height):
        super().is_off_screen(screen_width, screen_height)

    def fire(self, angle):
        self.draw()

        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED

        # print(f'DX: ----- {self.velocity.dx} -----')
        # print(f'DY: ----- {self.velocity.dy} -----\n')
