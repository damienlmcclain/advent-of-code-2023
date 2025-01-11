from unittest import TestCase

from aoc2023.day_solutions.day02 import (create_cube_dict,
                                         determine_possible_games)
from aoc2023.session_cookie import AOCD_SESSION_COOKIE


class Test(TestCase):
    max_allowed_colors = {'red': 12, 'green': 13, 'blue': 14}
    parsed_easy_input = [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
    ]

    def test_create_cube_dict(self):
        res = create_cube_dict(input_data=self.parsed_easy_input)
        expected_res = {
            1: {
                'blue': 6,
                'red': 4,
                'green': 2
            },
            2: {
                'blue': 4,
                'red': 1,
                'green': 3
            },
            3: {
                'blue': 6,
                'red': 20,
                'green': 13
            },
            4: {
                'blue': 15,
                'red': 14,
                'green': 3
            },
            5: {
                'blue': 2,
                'red': 6,
                'green': 3
            }
        }
        self.assertEqual(res, expected_res)

    def test_determine_possible_games_sum(self):
        res = determine_possible_games(
            max_of_each_color=self.max_allowed_colors,
            sum_or_product='sum',
            filename='day_solutions/tests/fixtures/day_02_easy_input.txt')
        self.assertEqual(res, 8)

    def test_determine_possible_games_sum_full_input(self):
        res = determine_possible_games(
            max_of_each_color=self.max_allowed_colors,
            sum_or_product='sum',
            day=2,
            year=2023,
            session_cookie=AOCD_SESSION_COOKIE)
        self.assertEqual(res, 2679)

    def test_determine_possible_games_product(self):
        res = determine_possible_games(
            max_of_each_color=self.max_allowed_colors,
            sum_or_product='product',
            filename='day_solutions/tests/fixtures/day_02_easy_input.txt')
        self.assertEqual(res, 2286)

    def test_determine_possible_games_product_full_input(self):
        res = determine_possible_games(
            max_of_each_color=self.max_allowed_colors,
            sum_or_product='product',
            day=2,
            year=2023,
            session_cookie=AOCD_SESSION_COOKIE)
        self.assertEqual(res, 77607)
