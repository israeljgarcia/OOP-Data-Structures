class GPA:
    """
    The GPA class stores a student's GPA within the range of
    0.0 and 4.0.

    member variables: gpa

    methods: __init__(), get_gpa(), set_gpa(value(float))
    """

    def __init__(self):
        """
        Initializes the gpa variable to 0.

        return: none
        """
        self.gpa = 0.0

    def get_gpa(self):
        """
        return: gpa
        """
        return self.gpa

    def set_gpa(self, value):
        """
        Assigns the gpa member variable according to the input.

        return: none
        """

        # The gpa can never be more than 4.0 or less than 0.0
        if value > 4.0:
            self.gpa = 4.0
        elif value < 0.0:
            self.gpa = 0.0

        # Sets gpa to the passed in value
        self.gpa = value

    def get_letter(self):
        """
        Calculates the letter grade based on the gpa

        return: string
        """

        if self.gpa < 1:
            return 'F'
        elif self.gpa < 2:
            return 'D'
        elif self.gpa < 3:
            return 'C'
        elif self.gpa < 4:
            return 'B'
        elif self.gpa == 4:
            return 'A'

    def set_letter(self, value):
        """
        Returns a letter grade based on the passed
        in value.

        return: string
        """
        if value == 'F':
            self.set_gpa(0.0)
        elif value == 'D':
            self.set_gpa(1.0)
        elif value == 'C':
            self.set_gpa(2.0)
        elif value == 'B':
            self.set_gpa(3.0)
        elif value == 'A':
            self.set_gpa(4.0)


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))


if __name__ == "__main__":
    main()
