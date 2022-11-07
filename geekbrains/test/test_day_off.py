import unittest
from geekbrains.src.geekbrains_task import day_off


class TestPositiveDayOff(unittest.TestCase):

    def test_5_return_False(self):
        assert day_off(5) is False

    def test_6_return_True(self):
        assert day_off(6) is True


class TestNegativeDayOff(unittest.TestCase):

    def test_8_return_None(self):
        assert day_off(8) == False
