class Ship:
    """
    This class defines a ship object with a position (x and y)
    and velocity (dx and dy)

    Member Variables: x(int), y (int), dx(int), dy(int)

    Methods: advance(), draw()
    """

    def __init__(self):
        """
        initializes all member variables to 0 when instantiated.
        """
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0

    def advance(self):
        """
        Adds the x velocity to position x and the y velocity to
        position y.

        Arguments: none

        Return: none
        """
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        """
        Prints the position of the ship
        """
        print(f'Drawing ship at ({self.x}, {self.y})')
