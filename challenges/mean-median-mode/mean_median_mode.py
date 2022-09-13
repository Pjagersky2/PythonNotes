"""Module for calculating mean, median, and mode of a dataset."""
from typing import List, Tuple


def calc_mean(numbers: List[int]) -> float:
    """
    Calculates the average of a list of numbers.

    Given a list of numbers, calculate the sum then divide them by the
    total amount of numbers and round it.

    Notes:
        Rounds to three decimal places.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        float: Float represented mean, rounded to three decimal places.

    Examples:
        >>> nums = [6, 9, 1, 2, 6, 3, 7]
        >>> mean = calc_mean(nums)
        >>> print(mean)
        4.857

    """

    mean = sum(numbers) / len(numbers)
    return round(mean, 3)


def calc_median(numbers: List[int]) -> float:
    """
    Find which number is in the middle.

    Given a list of numbers, sort the values.  If the total is odd then
    return the middle value.  If the total is even then return the
    average of the middle two values.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        float: Float represented median, rounded to two decimal places.

    Examples:
        >>> nums = [6, 9, 1, 2, 6, 3, 7]
        >>> median = calc_median(nums)
        >>> print(median)
        6.0

    """

    length = len(numbers)
    midpoint = length // 2
    sorted_numbers = sorted(numbers)

    if not length % 2:  # even
        upper_value = sorted_numbers[midpoint]
        lower_value = sorted_numbers[midpoint-1]
        median = (lower_value + upper_value) / 2
    else:  # odd
        median = sorted_numbers[midpoint]

    return float(round(median, 2))


def calc_mode(numbers: List[int]) -> List[int]:
    """
    Find the mode, number that appears the most.

    Given a list of numbers, calculate the frequency for each unique
    number.  Using the frequencies, find the number value with the
    highest frequency.

    Notes:
        There can be multiple modes.
        If all numbers are modes, there are no modes.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers representing modes, if any.

    Examples:
        >>> nums = [6, 9, 1, 2, 6, 3, 7]
        >>> mode = calc_mode(nums)
        >>> print(mode)
        [6]

    """

    unique_numbers = set(numbers)

    frequencies = {}
    for unique_number in unique_numbers:
        frequency = numbers.count(unique_number)
        frequencies[unique_number] = frequency

    highest = max(frequencies.values())

    modes = []
    for number, frequency in frequencies.items():
        if frequency == highest:
            modes.append(number)

    if len(modes) == len(unique_numbers):
        modes.clear()

    return modes


def solve_data_set(data_set: List[int]) -> Tuple[float, float, List[int]]:
    """
    Runs mean, median, and mode processes.

    This is where mean, median, and mode functions are called and return
    their results.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[float, float, List[int]]: A tuple containing mean,
                                        median, and mode.

    Examples:
        >>> nums = [6, 9, 1, 2, 6, 3, 7]
        >>> result = solve_data_set(nums)
        >>> print(result)
        (4.857, 6.0, [6])

    """

    mean = calc_mean(data_set)
    median = calc_median(data_set)
    mode = calc_mode(data_set)

    return mean, median, mode


def main() -> None:
    """
    Executes the main process.

    Hardcoded data sets that cover mean, median, and mode edge cases.
    Some of the edge cases covered were no modes, multiple modes, both
    even and odd data set lengths.

    """

    data_sets = (
        [6, 9, 1, 2, 6, 3, 7],
        [6, 9, 1, 2, 6, 3, 7, 4],
        [6, 9, 1, 2, 6, 3, 7, 4, 1],
        [6, 9, 1, 2, 3, 7, 4, 8]
    )

    for data_set in data_sets:
        result = solve_data_set(data_set)
        print(f"The mean, median, and mode is {result}")


if __name__ == "__main__":
    main()
