import re


def part_one_find_ints(filename):
    """
    Finds the ints in each line and returns them as a list of lists.

    Parameters
    ----------
    filename: str
        The name of the file to parse.

    Returns
    -------
    list of lists
        A list of lists containing the ints on each line.
    """
    with open(filename, encoding='utf-8') as file:
        input_data = file.read().split('\n')
    all_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    all_line_ints = []
    for line in input_data:
        line_ints = [character for character in line if character in all_nums]
        all_line_ints.append([int(character) for character in line_ints])
    return all_line_ints


def part_two_find_nums(filename):
    """
    Finds the numbers in each line, either as ints or written out, and returns them as a list of lists.

    Parameters
    ----------
    filename: str
        The name of the file to parse.

    Returns
    -------
    list of lists
        A list of lists containing the ints on each line.
    """
    with open(filename, encoding='utf-8') as file:
        input_data = file.read().split('\n')
    all_ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    all_nums_as_strs = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
                        'eight': 8, 'nine': 9}
    all_line_ints = []
    for line in input_data:
        str_num = ''
        line_nums = {}
        altered_line = line
        line_index = 0
        for character in line:
            if character in all_ints:
                line_nums[line_index] = int(character)
            line_index += 1
        for key, value in all_nums_as_strs.items():
            for index in re.finditer(key, line):
                line_nums[int(index.start())] = value
        myKeys = list(line_nums.keys())
        myKeys.sort()
        sorted_nums_dict = {i: line_nums[i] for i in myKeys}
        sorted_nums = list(sorted_nums_dict.values())
        all_line_ints.append(sorted_nums)
    return all_line_ints


def find_calibration_value(calibration_values_list):
    """
    Given a list of lists of values, finds the original elf calibration values and sums them.

    Parameters
    ----------
    calibration_values_list: list of lists
        The list of art-ified calibration values.

    Returns
    ----------
    int
        The sum of the correct calibration values.
    """
    calibration_value_sum = 0
    for line in calibration_values_list:
        calibration_value = 0
        if len(line) == 1:
            calibration_value = line[0] * 10 + line[0]
        elif len(line) > 1:
            calibration_value = line[0] * 10 + line[-1]
        calibration_value_sum += calibration_value

    return calibration_value_sum

part_one_ints = part_one_find_ints(filename='day_1_input.txt')
print(f'The answer to day one, part one is {find_calibration_value(part_one_ints)}')

part_two_ints = part_two_find_nums(filename='day_1_input.txt')
print(f'The answer to day one, part two is {find_calibration_value(part_two_ints)}')