"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.
Sorts a list of numbers.
"""

def sort(numbers):
    """
    Sort numbers by selction sort
    """
    # This will loop n times according to the size of the array starting at the
    # Last index and ending at 0
    for i in range(len(numbers) - 1, 0, -1):
        # Sets the biggest index to 0
        biggest_index = 0

        # This loops i times, so only unsorted indexes are looped through.
        for j in range(i):
          
          # Compares the next index value to the current value at biggest index
          if numbers[biggest_index] < numbers[j + 1]:

            # Sets a new biggest index
            biggest_index = (j + 1)

        # Swaps the current last index (i) with the biggest value's index
        numbers[i], numbers[biggest_index] = numbers[biggest_index], numbers[i]

def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers

def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)

def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)

if __name__ == "__main__":
    main()