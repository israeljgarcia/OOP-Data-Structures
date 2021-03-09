class NegativeNumberError(Exception):
    """
    This class is used to handle errors caused by negative
    numbers
    """

    def __init__(self):
        super().__init__()


def get_inverse(n):

    # Raise a value error if n is not a float
    if type(n) != float:
        raise ValueError()

    # Raise a zero division error is n is 0
    if n == 0:
        raise ZeroDivisionError()

    # raise a negative number error if n is negative
    if n < 0:
        raise NegativeNumberError()

    return 1/n


def main():
    # Try catch block to catch any expected errors
    try:
        number = float(input("Enter a number: "))
        print(get_inverse(number))
    except ValueError:
        print("Error: The value must be a number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except NegativeNumberError:
        print("Error: The value cannot be negative")


if __name__ == "__main__":
    main()
