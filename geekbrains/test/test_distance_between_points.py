import unittest
from geekbrains.src.geekbrains_task import distance_between_points


class TestPositiveDistanceBetweenPoints(unittest.TestCase):

    def test_1_1_2_2_return_float(self):
        assert distance_between_points(1, 1, 2, 2) == 1.4142135623730951


class TestNegativeDistanceBetweenPoints(unittest.TestCase):

    def test_0_0_0_0_return_0(self):
        assert distance_between_points(0, 0, 0, 0) == 0.0
