import unittest
from geekbrains.src.geekbrains_task import range_coordinates_of_points


class TestPositiveRangeCoordinatesOfPoints(unittest.TestCase):

    def test_2_return_answer(self):
        assert range_coordinates_of_points(2) == 'x=(-∞;0], y=[0;∞)'

    def test_3_return_answer(self):
        assert range_coordinates_of_points(4) == 'x=[0;∞), y=(-∞;0]'
