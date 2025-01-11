from unittest import TestCase

from aoc2023.utils import parse_input


class Test(TestCase):

    def test_parse_input(self):
        res = parse_input(
            filename='day_solutions/tests/fixtures/day_01_part_1_easy_input.txt'
        )
        expected_res = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
        self.assertEqual(res, expected_res)

        res = parse_input(
            filename='day_solutions/tests/fixtures/day_01_part_2_easy_input.txt'
        )
        expected_res = [
            'two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four',
            '4nineeightseven2', 'zoneight234', '7pqrstsixteen'
        ]
        self.assertEqual(res, expected_res)

        # should error
        res = parse_input()
        expected_res = 'Please enter a valid combination of inputs: either ' \
                       'a filename to pull from locally or a day, year, and ' \
                       'session_cookie.'
        self.assertEqual(res, expected_res)
