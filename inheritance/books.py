class Book:
    """
    Base class for book objects. It includes the basics: title, author, publication year,
    prompting book info, and displaying book info.

    Member Variables: title(string), author(string), year(int)

    Methods: prompt_book_info(), display_book_info()
    """

    def __init__(self):
        """
        Sets member variables to empty strings or 0
        """
        self.title = ''
        self.author = ''
        self.publication_year = 0

    def prompt_book_info(self):
        """
        Asks the user for the book's title, author, and publication year.
        Sets the variables accordingly.

        Return: none
        """
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = int(input("Publication Year: "))

    def display_book_info(self):
        """
        Prints the book's info in this format:
        "Title (year) by Author"

        Return: none
        """
        print(f'{self.title} ({self.publication_year}) by {self.author}')


class TextBook(Book):
    """
    A child of the Book class, but it includes a subject in the book
    info. Additionally, it can prompt the user for a subject and display
    the subject.

    Member Varbiables: (See Book class), subject(string)

    Methods: (See Book class), prompt_subject(), display_subject()
    """

    def __init__(self):
        """
        Calls the Book __init__ method and also initializes
        subject to a blank string.
        """
        super().__init__()

        self.subject = ''

    def prompt_subject(self):
        """
        Prompts the user to enter a subject and saves it to
        the subject variable.

        Return: none
        """
        self.subject = input("Subject: ")

    def display_subject(self):
        """
        Prints the TextBook's subject in this format:
        "Subject: subject"
        """
        print(f'Subject: {self.subject}')


class PictureBook(Book):
    """
    A child of the Book class, but adds an illustrator member variable.
    It can also prompt the user for an illustrator and display it.

    Member Variables: (See Book class), illustrator(string)

    Methods: (See Book class), prompt_illustrator(), display_illustrator() 
    """

    def __init__(self):
        """
        Calls the Book class __init__ method. and initilizes the
        illustrator variable to an empty string.
        """
        super().__init__()

        self.illustrator = ''

    def prompt_illustrator(self):
        """
        Prompts the user to enter an illustrator and sets that input
        to the illustrator variable.

        Return: none
        """
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        """
        Displays the illustator in this format:
        "Illustrator: illustrator"
        """
        print(f'Illustrator: {self.illustrator}')


def main():

    # Creates a Book object assigned to book
    book = Book()

    # Prompts the user to enter information about the book
    book.prompt_book_info()
    print()

    # Prints the Book's author, title, and publication year
    book.display_book_info()
    print()

    # Creates a TextBook object assigned to textbook
    textbook = TextBook()
    textbook.prompt_book_info()

    # Prompts the user for a subject
    textbook.prompt_subject()
    print()
    textbook.display_book_info()

    # Prints the TextBook's subject
    textbook.display_subject()
    print()

    # Creates a PictureBook object and assigns it to picturebook
    picturebook = PictureBook()
    picturebook.prompt_book_info()

    # Prompts the user to enter an illustrator
    picturebook.prompt_illustrator()
    print()

    picturebook.display_book_info()

    # Prints the PictureBook's illustrator
    picturebook.display_illustrator()


if __name__ == '__main__':
    main()
