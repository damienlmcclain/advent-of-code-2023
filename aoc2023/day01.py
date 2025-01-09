import aocd
import os
import re


def parse_input(day: int = None,
                year: int = None,
                session_cookie: str = None,
                filename: str = None) -> list or str:
    """
    Finds the ints in each line and returns them as a list of lists.

    Parameters
    ----------
    day
        The day to pull data for.
    year
        The year to pull data for.
    session_cookie
        The AOC session cookie for pulling data.
    filename
        If input, the name of the file to parse instead of pulling data using
        the day/year.

    Returns
    -------
    A list of each line in the pulled data or file as a str.
    """

    if filename:
        with open(filename, encoding='utf-8') as file:
            input_data = file.read().split('\n')
    elif day and year and session_cookie:
        os.environ['AOC_SESSION'] = session_cookie
        data = aocd.get_data(day=day, year=year)
        input_data = data.split('\n')
    else:
        return 'Please enter a valid combination of inputs: either a ' \
               'filename to pull from locally or a day, year, and ' \
               'session_cookie.'
    return input_data


def part_one_find_ints(input_data: list) -> list:
    """
    Finds the calibration value ints in each line and returns them as a list
    of lists.

    Parameters
    ----------
    input_data
        The list of calibration values to parse.

    Returns
    -------
    A list of lists containing the calibration value ints on each line.
    """

    all_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    all_line_ints = []
    for line in input_data:
        line_ints = [character for character in line if character in all_nums]
        all_line_ints.append([int(character) for character in line_ints])
    return all_line_ints


def part_two_find_nums(input_data: list) -> list:
    """
    Finds the numbers in each line, either as ints or written out as strs,
    and returns them as a list of lists.

    Parameters
    ----------
    input_data
        The list of calibration values to parse.

    Returns
    -------
    A list of lists containing the ints on each line, sorted by their
    index on the line.
    """

    all_ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    all_nums_as_strs = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    all_line_ints = []
    for line in input_data:
        line_nums = {}
        for line_index, character in enumerate(line):
            if character in all_ints:
                line_nums[line_index] = int(character)
        for key, value in all_nums_as_strs.items():
            for index in re.finditer(key, line):
                line_nums[int(index.start())] = value
        myKeys = list(line_nums.keys())
        myKeys.sort()
        sorted_nums_dict = {i: line_nums[i] for i in myKeys}
        sorted_nums = list(sorted_nums_dict.values())
        all_line_ints.append(sorted_nums)
    return all_line_ints


def find_calibration_value(part: int,
                           day: int = None,
                           year: int = None,
                           session_cookie: str = None,
                           filename: str = None) -> int or str:
    """
    Given a list of lists of values, finds the original elf calibration values
    and sums them.

    Parameters
    ----------
    part
        Part one or two for the day. Determines how the data is parsed.
    day
        The day to pull data for.
    year
        The year to pull data for.
    session_cookie
        The AOC session cookie for pulling data.
    filename
        If input, the name of the file to parse instead of pulling data using
        the day/year.

    Returns
    ----------
    The sum of the correct calibration values or a str error.
    """
    if filename:
        massaged_input_data = parse_input(filename=filename)
    elif day and year and session_cookie:
        massaged_input_data = parse_input(day=day,
                                          year=year,
                                          session_cookie=session_cookie)
    elif not day or not year:
        return 'You have not entered either a filename or a day and year ' \
               'combination. Please enter one of the two and retry.'
    elif not session_cookie:
        return 'You have not entered either a filename or a session cookie. ' \
               'Please enter one of the two and retry.'

    if part == 1:
        nums_to_parse = part_one_find_ints(input_data=massaged_input_data)
    elif part == 2:
        nums_to_parse = part_two_find_nums(input_data=massaged_input_data)
    else:
        return f'Please enter 1 or 2 as the part. {part} is not a valid part.'

    calibration_value_sum = 0
    for line in nums_to_parse:
        calibration_value = 0
        if len(line) == 1:
            calibration_value = line[0] * 10 + line[0]
        elif len(line) > 1:
            calibration_value = line[0] * 10 + line[-1]
        calibration_value_sum += calibration_value

    return calibration_value_sum
