import arcade


class DemoApp(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        self.x = 100

    # arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_filled(self.x, 100, 50, 20, arcade.color.WHITE)

        self.x += 1

    def update(self, delta_time: float):
        pass


window = DemoApp(500, 400)
arcade.run()
