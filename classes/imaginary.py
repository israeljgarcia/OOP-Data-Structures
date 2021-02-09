class Complex:
    """
    Class for creating complex numbers
    """

    def __init__(self):
        """
        Initializes the real value and imaginary value to zero
        """
        self.real = 0
        self.imaginary = 0

    def prompt(self):
        """
        Prompts the user to set the real and imaginary values
        """
        self.real = int(input("Please enter the real part: "))
        self.imaginary = int(input("Please enter the imaginary part: "))

    def display(self):
        """
        Displays the complex number in this format: 0 + 0i
        """
        print(f'{self.real} + {self.imaginary}i')
