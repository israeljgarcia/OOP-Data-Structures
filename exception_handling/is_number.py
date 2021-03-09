def main():
    """
    This program takes a user's number input and prints
    that number multiplied by 2.
    """

    # Setting necessary global variables
    is_valid = False
    num = ''

    # This loop runs until the user enters a valid number
    while not is_valid:
        try:
            num = int(input("Enter a number: "))
            is_valid = True

        # If the value is not the correct type, then this will run
        except ValueError:
            print("The value entered is not valid")

    # Print the result
    print(f'The result is: {num * 2}')


if __name__ == "__main__":
    main()
