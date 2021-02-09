class Robot:
    """
    The robot class can be used to create a robot that can move
    up, down, left, and right. It can also fire lasers and 
    report it's status.

    member variables: xpos, ypos, fuel, active

    member functions: move_left, move_right, move_up, 
    move_down, fire, status, power_switch, command,
    check_fuel
    """

    def __init__(self):
        """
        Sets all member variables to default settings when created
        """
        self.xpos = 10
        self.ypos = 10
        self.fuel = 100
        self.active = True

    def move_left(self):
        """
        Checks for sufficient fuel.
        Subtracts 1 from the x position.
        Subtracts 5 fuel.
        """
        if self.check_fuel(5):
            print("Insufficient fuel to perform action")
        else:
            self.xpos -= 1
            self.fuel -= 5

    def move_right(self):
        """
        Checks for sufficient fuel.
        Adds 1 to the x position.
        Subtracts 5 fuel.
        """
        if self.check_fuel(5):
            print("Insufficient fuel to perform action")
        else:
            self.xpos += 1
            self.fuel -= 5

    def move_up(self):
        """
        Checks for sufficient fuel.
        Subtracts 1 to the y position.
        Subtracts 5 fuel.
        """
        if self.check_fuel(5):
            print("Insufficient fuel to perform action")
        else:
            self.ypos -= 1
            self.fuel -= 5

    def move_down(self):
        """
        Checks for sufficient fuel.
        Adds 1 from the y position.
        Subtracts 5 fuel.
        """
        if self.check_fuel(5):
            print("Insufficient fuel to perform action")
        else:
            self.ypos += 1
            self.fuel -= 5

    def fire(self):
        """
        Checks for sufficient fuel.
        Subtracts 15 fuel
        Prints "Pew! Pew!"
        """
        if self.check_fuel(15):
            print("Insufficient fuel to perform action")
        else:
            self.fuel -= 15
            print("Pew! Pew!")

    def status(self):
        """
        Prints the x position, y position, and fuel like this:
        (x, y) - Fuel: 40
        """
        print(f'({self.xpos}, {self.ypos}) - Fuel: {self.fuel}')

    def power_switch(self):
        """
        Turns the robot on or off. Prints Goodbye
        if the robot is turning off.
        """
        self.active = not self.active
        if not self.active:
            print("Goodbye.")

    def command(self, action):
        """
        Argument: action - Takes in a robot action as a string

        valid actions: "left", "right", "up", "down", "status",
        "fire", "quit"

        The actions are stored in a dictionary. Each action 
        corresponds to an appropriate member functions e.g.:
        "left" => self.move_left
        "fire" => self.fire

        returns: member function or nothing
        """
        switch = {
            "left": self.move_left,
            "right": self.move_right,
            "up": self.move_up,
            "down": self.move_down,
            "status": self.status,
            "fire": self.fire,
            "quit": self.power_switch
        }

        if action in switch:
            return switch[action]()

    def check_fuel(self, cost):
        """
        Checks if cost of fuel is greater
        than remaining fuel.

        returns: boolean value | True or False
        """
        return cost > self.fuel


def main():
    robot = Robot()

    while robot.active:
        action = input("Enter command: ")
        robot.command(action)


if __name__ == "__main__":
    main()
