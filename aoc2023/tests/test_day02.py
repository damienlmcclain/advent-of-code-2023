from unittest import TestCase

from aoc2023.day02 import determine_possible_games, parse_input
from aoc2023.session_cookie import AOCD_SESSION_COOKIE


class Test(TestCase):
    max_allowed_colors = {'red': 12, 'green': 13, 'blue': 14}

    def test_parse_input(self):
        res = parse_input(filename='tests/fixtures/day_02_easy_input.txt')
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

    def test_determine_possible_games(self):
        res = determine_possible_games(
            max_of_each_color=self.max_allowed_colors,
            filename='tests/fixtures/day_02_easy_input.txt')
        self.assertEqual(res, 8)

    def test_determine_possible_games_full_input(self):
        res = determine_possible_games(
            max_of_each_color=self.max_allowed_colors,
            day=2,
            year=2023,
            session_cookie=AOCD_SESSION_COOKIE)
        self.assertEqual(res, 2679)
