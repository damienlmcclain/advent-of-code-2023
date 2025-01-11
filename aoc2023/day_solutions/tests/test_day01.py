from unittest import TestCase

from aoc2023.day_solutions.day01 import (find_calibration_value,
                                         part_one_find_ints,
                                         part_two_find_nums)
from aoc2023.session_cookie import AOCD_SESSION_COOKIE
from aoc2023.utils import parse_input


class Test(TestCase):

    def test_part_one_find_ints(self):
        input_data = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
        res = part_one_find_ints(input_data=input_data)
        expected_res = [[1, 2], [3, 8], [1, 2, 3, 4, 5], [7]]
        self.assertEqual(res, expected_res)

    def test_day_01_part_1_easy_input(self):
        res = find_calibration_value(
            part=1,
            filename='day_solutions/tests/fixtures/day_01_part_1_easy_input.txt'
        )
        self.assertEqual(res, 142)

    def test_day_01_part_1(self):
        res = find_calibration_value(part=1,
                                     day=1,
                                     year=2023,
                                     session_cookie=AOCD_SESSION_COOKIE)
        self.assertEqual(res, 54331)

    def test_part_two_find_nums(self):
        input_data = parse_input(
            filename='day_solutions/tests/fixtures/day_01_part_2_easy_input.txt'
        )
        res = part_two_find_nums(input_data=input_data)
        expected_res = [[2, 1, 9], [8, 2, 3], [1, 2, 3], [2, 1, 3, 4],
                        [4, 9, 8, 7, 2], [1, 8, 2, 3, 4], [7, 6]]
        self.assertEqual(res, expected_res)

    def test_day_01_part_2_easy_input(self):
        res = find_calibration_value(
            part=2,
            filename='day_solutions/tests/fixtures/day_01_part_2_easy_input.txt'
        )
        self.assertEqual(res, 281)

    def test_day_01_part_2(self):
        res = find_calibration_value(part=2,
                                     day=1,
                                     year=2023,
                                     session_cookie=AOCD_SESSION_COOKIE)
        self.assertEqual(res, 54518)

    def test_find_calibration_value_error(self):
        res = find_calibration_value(part=1)
        expected_res = 'You have not entered either a filename or a day ' \
                       'and year combination. Please enter one of the ' \
                       'two and retry.'
        self.assertEqual(res, expected_res)

        res = find_calibration_value(part=1, day=1, year=2023)
        expected_res = 'You have not entered either a filename or a ' \
                       'session cookie. Please enter one of the two and ' \
                       'retry.'
        self.assertEqual(res, expected_res)

        res = find_calibration_value(part=3,
                                     day=1,
                                     year=2023,
                                     session_cookie=AOCD_SESSION_COOKIE)
        expected_res = 'Please enter 1 or 2 as the part. 3 is not a valid ' \
                       'part.'
        self.assertEqual(res, expected_res)
