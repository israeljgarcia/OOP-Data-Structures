class Phone:
    """
    The Phone class creates Phone objects that have an area code,
    prefix, and suffix numbers

    Member Variables: area_code(int), prefix(int), suffix(int)

    Methods: prompt_number(), display()
    """

    def __init__(self):
        """
        Sets member variables to zero
        """
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):
        """
        Prompts the user to enter an area code, prefix, and a suffix number

        Return: none
        """
        self.area_code = int(input("Area code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))

    def display(self):
        """
        Prints the phone number in this format:
        Phone info:
        (123)456-7890

        Return: none
        """
        print('Phone info:')
        print(f'({self.area_code}){self.prefix}-{self.suffix}')


class SmartPhone(Phone):
    """
    The SmartPhone class has everything the Phone class has, but
    is also capable of holding an email.
    """

    def __init__(self):
        """
        Initializes all Phone member varbiables (see Phone class)
        and sets email to an empty string
        """
        super().__init__()
        self.email = ''

    def prompt(self):
        """
        Prompts the user for phone information (see Phone class)
        and the user is prompted to enter an email to set

        Return: none
        """
        super().prompt_number()
        self.email = input("Email: ")

    def display(self):
        """
        Prints the phone number (see Phone class) and prints the 
        phone's email in this format:
        Phone info:
        (123)456-7890
        email@email.com
        """
        super().display()
        print(f'Email: {self.email}')


def main():
    my_phone = Phone()

    print("Phone:")
    my_phone.prompt_number()
    print()
    my_phone.display()
    print()

    smart_phone = SmartPhone()

    print("Smart Phone:")
    smart_phone.prompt()
    print()
    smart_phone.display()


if __name__ == '__main__':
    main()
