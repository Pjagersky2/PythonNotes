"""Module for calculating mean, median, and mode of a dataset"""


def calc_mean(numbers):
    """
    Calculate the sum of numbers
    Divide the sum by the length of numbers
    """

    # total = 0
    # for number in numbers:
    #     total += number

    # mean = total / len(numbers)
    # mean = round(mean, 3)

    # return mean

    return round((sum(numbers) / len(numbers)), 3)


def calc_median(numbers):
    """
    Sort the data set
    Figure out if its even or odd
    Return middle index for odd
    Return average of two middle indexes for even
    """

    length = len(numbers)
    midpoint = length // 2
    sorted_numbers = sorted(numbers)
    if not length % 2:
        # even
        upper_value = sorted_numbers[midpoint]
        lower_value = sorted_numbers[midpoint-1]
        median = (lower_value + upper_value) / 2
    else:
        # odd
        median = sorted_numbers[midpoint]

    return round(median, 2)


def calc_mode(numbers):
    """
    Find which number appears the most

    Start with a list of numbers

    loop through unique numbers:
        insert frequency and unique number in to a dictionary

    use frequencies to calculate the highest frequency

    loop through number, frequency in frequencies:
        if frequency is equal to highest:
            add the number to list of modes

    Return a list of modes
    """

    frequencies = {}
    for unique_number in set(numbers):
        frequency = numbers.count(unique_number)
        frequencies[unique_number] = frequency

    highest = -1
    for frequency in frequencies.values():
        if highest < frequency:
            highest = frequency

    no_mode = True
    for frequency in frequencies.values():
        if frequency != highest:
            no_mode = False

    modes = []
    for number, frequency in frequencies.items():
        if frequency == highest:
            modes.append(number)

    return [] if no_mode else modes


def solve_data_set(data_set):
    mean = calc_mean(data_set)
    median = calc_median(data_set)
    mode = calc_mode(data_set)

    return mean, median, mode


def main():
    """Runs the main process"""

    data_set_one = [6, 9, 1, 2, 6, 3, 7]
    data_set_two = [6, 9, 1, 2, 6, 3, 7, 4]
    data_set_three = [6, 9, 1, 2, 6, 3, 7, 4, 1]
    data_set_four = [6, 9, 1, 2, 3, 7, 4, 8]

    data_sets = (
        data_set_one,
        data_set_two,
        data_set_three,
        data_set_four
    )

    for data_set in data_sets:
        result = solve_data_set(data_set)
        print(result)


if __name__ == "__main__":
    main()
