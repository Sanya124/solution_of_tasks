import unittest
from dzen.src.dzen_task import diving_17_and_19


class TestPositiveDiving17And19(unittest.TestCase):

	def test_17_return_0(self):
		assert diving_17_and_19(17) == 0

	def test_19_return_0(self):
		assert diving_17_and_19(19) == 0

	def test_2261_return_1(self):
		assert diving_17_and_19(2261) == 1


class TestNegativeDiving17And19(unittest.TestCase):

	def test_minus_1_return_0(self):
		assert diving_17_and_19(-1) == 0

	def test_0_return_0(self):
		assert diving_17_and_19(0) == 0
