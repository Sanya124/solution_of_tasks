import unittest
from geekbrains.src.geekbrains_task import list_factorial


class TestPositiveListFactorial(unittest.TestCase):

    def test_2_return_2(self):
        assert list_factorial(2) == [1, 2]

    def test_0_return_1(self):
        assert list_factorial(0) == []


class TestNegativeListFactorial(unittest.TestCase):

    def test_minus_1_return_error(self):
        assert list_factorial(-1) == []
