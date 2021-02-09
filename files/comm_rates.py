# import math

# fileref = open('rates_small.csv', 'r')
# header_array = fileref.readline().split(',')
# company_name_index = 2
# company_zip_index = 0
# state_index = 3
# comm_rates_index = header_array.index('comm_rate')

# lowest_rate = math.inf
# highest_rate = -math.inf
# lowest_company = ''
# higest_company = ''


# count = 0
# sum = 0

# for line in fileref:
#     current_line = line.split(',')
#     current_rate = float(current_line[comm_rates_index])
#     # lowest_rate = lowest_rate if lowest_rate < current_rate else current_rate
#     # highest_rate = highest_rate if highest_rate > current_rate else current_rate
#     if current_rate < lowest_rate:
#         lowest_rate = current_rate
#         lowest_company = f'{current_line[company_name_index]} ({current_line[company_zip_index]}, {current_line[state_index]}) - {current_rate}'
#     if current_rate > highest_rate:
#         highest_rate = current_rate
#         highest_company = f'{current_line[company_name_index]} ({current_line[company_zip_index]}, {current_line[state_index]}) - {current_rate}'
#     sum += current_rate
#     count += 1

# print(f'The average commercial rate is: {sum/count}\n')
# print(f'The highest rate is: \n{highest_company}\n')
# print(f'The lowest rate is: \n{lowest_company}\n')


# fileref.close()
import math


def main():
    # Setting lowest rate and highest rate globally
    # To compare with the current rate being read from
    # the file
    lowest_rate = math.inf
    highest_rate = -math.inf

    # These variables will change as new lower or
    # higher rates are found
    lowest_company = ''
    highest_company = ''

    # Keeps track of the sum of rates and number of
    # lines to calculate the average
    total = 0
    count = 0

    # Prompts the user for a file path
    file_path = prompt_filepath()

    # Opens the file and sets variable as a reference
    file_reference = open(file_path, 'r')

    # Reads the first line of the file and returns necessary
    # index values of the header as an array
    file_header_indexes = get_file_header(file_reference)

    for line in file_reference:
        # Sets current line to an array of words
        current_line = line.split(',')
        # if current_line == ['']:
        #     break

        # Sets the value at index 6 to the current rate
        current_rate = float(current_line[file_header_indexes[3]])

        # Compares the lowest rate so far with the current rate
        if compare_low_rate(lowest_rate, current_rate):
            lowest_rate = current_rate

            # If rates change, the lowest company's details will be updated
            lowest_company = get_company_details(
                current_line, file_header_indexes)

        # Same as compare low rates, but inversed
        if compare_high_rate(highest_rate, current_rate):
            highest_rate = current_rate
            highest_company = get_company_details(
                current_line, file_header_indexes)

        # Counters
        total += current_rate
        count += 1

    file_reference.close()
    print(
        f'\nThe average commercial rate is: {calculate_average(total, count)}\n')
    print(f'The highest rate is:\n{highest_company}\n')
    print(f'The lowest rate is:\n{lowest_company}\n')


def prompt_filepath():
    """
    Prompts the user to enter a file path

    returns: the file path entered
    """
    file_path = input('Please enter the data file: ')
    return file_path


def get_file_header(file_reference):
    """
    Opens the file specified and finds the indexes for 
    comm_rate_index, company_name_index, company_zip_index, and state_index 

    Arguments: file_reference(an opened file)

    returns: array of index values [company_name_index, company_zip_index, state_index, comm_rate_index]
    """
    # Splits the first line of the file into an array
    header_array = file_reference.readline().split(',')

    # Sets indexes according to header names
    company_name_index = header_array.index('utility_name')
    company_zip_index = header_array.index('zip')
    state_index = header_array.index('state')
    comm_rate_index = header_array.index('comm_rate')

    return [company_name_index, company_zip_index, state_index, comm_rate_index]


def compare_low_rate(lowest_rate, compare_rate):
    """
    Compares the current lowest rate with another rate

    Arguments: lowest_rate(number), compare_rate(number)

    returns: true or false
    """
    return lowest_rate > compare_rate


def compare_high_rate(highest_rate, compare_rate):
    """
    Compares the current highest rate with another rate

    Arguments: lowest_rate(number), compare_rate(number)

    returns: true or false
    """
    return highest_rate < compare_rate


def get_company_details(company, detail_indexes):
    """
    Gets the values from the company array at the indexes provided by the
    detail_indexes array

    Arguments: company(array), detail_indexes(array)

    returns: the selected company details as a string
    """
    company_details = []

    # Loops through the number of detail_indexes and appends
    # the values specified by detail_indexes
    # to the company_details array
    for index, value in enumerate(detail_indexes):
        company_details.append(company[detail_indexes[index]])

    rate = float(company_details[3])
    if rate == 0:
        rate = "{:.1f}".format(rate)

    return f'{company_details[0]} ({company_details[1]}, {company_details[2]}) - ${rate}'


def calculate_average(sum, total):
    """
    Calculates the average based on the sum and number of items (total)

    Arguments: sum(number), total(number)

    returns: The sum divided by the total
    """
    return sum / total


if __name__ == '__main__':
    main()
