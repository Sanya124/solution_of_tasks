import unittest
from geekbrains.src.geekbrains_task import sum_of_digits_of_number


class TestPositiveSumOfDigitsOfNumber(unittest.TestCase):

    def test_str_return_14(self):
        assert sum_of_digits_of_number('5.90') == 14

    def test_str_return_1(self):
        assert sum_of_digits_of_number('0.100000001') == 2
