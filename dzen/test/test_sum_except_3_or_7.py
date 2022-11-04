import unittest
from dzen.src.dzen_task import *


class TestPositiveSumExcept3Or7(unittest.TestCase):

	def test_1_return_1(self):
		assert sum_except_3_or_7(1) == 1

	def test_3_return_3(self):
		assert sum_except_3_or_7(3) == 3

	def test_4_return_3(self):
		assert sum_except_3_or_7(4) == 7


class TestNegativeSumExcept3Or7(unittest.TestCase):

	def test_minus_1_return_0(self):
		assert sum_except_3_or_7(-1) == 0

	def test_0_return_0(self):
		assert sum_except_3_or_7(0) == 0
