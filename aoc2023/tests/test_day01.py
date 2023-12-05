from unittest import TestCase

from aoc2023.day01 import part_one_find_ints, part_two_find_nums, find_calibration_value


class Test(TestCase):
    def test_day_01_part_1_easy_input(self):
        res = part_one_find_ints(
            filename='fixtures/day_01_part_1_easy_input.txt')
        expected_res = [[1, 2], [3, 8], [1, 2, 3, 4, 5], [7]]
        self.assertEqual(res, expected_res)

        res = find_calibration_value(calibration_values_list=res)
        self.assertEqual(res, 142)

    def test_day_01_part_1(self):
        ints = part_one_find_ints(filename='fixtures/day_01_input.txt')
        res = find_calibration_value(calibration_values_list=ints)
        self.assertEqual(res, 54990)

    def test_day_01_part_2_easy_input(self):
        res = part_two_find_nums(
            filename='fixtures/day_01_part_2_easy_input.txt')
        expected_res = [[2, 1, 9], [8, 2, 3], [1, 2, 3], [2, 1, 3, 4],
                        [4, 9, 8, 7, 2], [1, 8, 2, 3, 4], [7, 6]]
        self.assertEqual(res, expected_res)

        res = find_calibration_value(calibration_values_list=res)
        self.assertEqual(res, 281)

    def test_day_01_part_2(self):
        nums = part_two_find_nums(filename='fixtures/day_01_input.txt')
        res = find_calibration_value(calibration_values_list=nums)
        self.assertEqual(res, 54473)
