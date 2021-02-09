"""
Description: 
    This program counts the number of occurances of a user-entered word
    in a text file. Good for basic file parsing homework.
"""


def main():
    file = prompt_filename()
    word = prompt_word()

    print(f'Opening file {file}')
    print(f'There are {parse_file(file, word)} occurances of say.')


def prompt_filename():
    """Prompts the user to enter a file path and returns that path as a string"""
    file_path = input("Enter a file path: ")
    return file_path


def prompt_word():
    """Prompts for a word, returns that word as a string"""
    get_word = input("Enter a word to check for: ")
    return get_word


def parse_file(file, check_word):
    """Counter variable"""
    occurances = 0

    """Sets a reference to the opened file"""
    fileref = open(file, "r")

    """Nested for loop to iterate through each word"""
    for line in fileref:
        for word in line.split():
            """Checks if the current word contains the user's word"""
            if check_word.lower() in word.lower():
                occurances += 1
    fileref.close()

    return occurances


if __name__ == "__main__":
    main()
