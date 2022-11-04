import unittest
from dzen.src.dzen_task import _diving, _minus_and_diving


class TestDiving(unittest.TestCase):

    def test_1_1_return_true(self):
        assert _diving(1, 1) == True

    def test_1_2_return_false(self):
        assert _diving(1, 2) == False


class TestMinusAndDiving(unittest.TestCase):

    def test_1_1_return_true(self):
        assert _minus_and_diving(1, 1) == True

    def test_1_2_return_false(self):
        assert _minus_and_diving(1, 2) == False
