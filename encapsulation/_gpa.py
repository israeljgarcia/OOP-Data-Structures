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
        self._gpa = 0.0

    def _get_gpa(self):
        """
        return: gpa
        """
        return self._gpa

    def _set_gpa(self, value):
        """
        Assigns the gpa member variable according to the input.

        return: none
        """

        # The gpa can never be more than 4.0 or less than 0.0
        if value > 4.0:
            self._gpa = 4.0
        elif value < 0.0:
            self._gpa = 0.0

        # Sets gpa to the passed in value
        self._gpa = value

    def _get_letter(self):
        """
        Calculates the letter grade based on the gpa

        return: string
        """

        if self._get_gpa() < 1:
            return 'F'
        elif self._get_gpa() < 2:
            return 'D'
        elif self._get_gpa() < 3:
            return 'C'
        elif self._get_gpa() < 4:
            return 'B'
        elif self._get_gpa() == 4:
            return 'A'

    def _set_letter(self, value):
        """
        Returns a letter grade based on the passed
        in value.

        return: string
        """
        if value == 'F':
            self._set_gpa(0.0)
        elif value == 'D':
            self._set_gpa(1.0)
        elif value == 'C':
            self._set_gpa(2.0)
        elif value == 'B':
            self._set_gpa(3.0)
        elif value == 'A':
            self._set_gpa(4.0)

    @property
    def letter(self):
        return self._get_letter()

    @letter.setter
    def letter(self, value):
        self._set_letter(value)

    gpa = property(_get_gpa, _set_gpa)


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))


if __name__ == "__main__":
    main()
