import unittest
from geekbrains.src.geekbrains_task import sum_of_list_to_formula


class TestPositiveSumOfListToFormula(unittest.TestCase):

    def test_0_return_2(self):
        assert sum_of_list_to_formula(1) == 2.0


class TestNegativeSumOfListToFormula(unittest.TestCase):

    def test_minus_1_return_str(self):
        assert sum_of_list_to_formula(0) == 0
