import unittest
from geekbrains.src.geekbrains_task import number_quarter_of_plane


class TestPositiveNumberQuarterOfPlane(unittest.TestCase):

    def test_1_1_return_1(self):
        assert number_quarter_of_plane(1, 1) == 1

    def test_minus_1_minus_1_return_3(self):
        assert number_quarter_of_plane(-1, -1) == 3


class TestNegativeNumberQuarterOfPlane(unittest.TestCase):

    def test_0_0_return_none(self):
        assert number_quarter_of_plane(0, 0) is None

    def test_1_0_return_4(self):
        assert number_quarter_of_plane(1, 0) == 4

    def test_0_1_return_none(self):
        assert number_quarter_of_plane(0, 1) is None
        # Проверяется два условия x > 0 или x < 0 из этого следует, что тест будет None
