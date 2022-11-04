import unittest
from dzen.src.dzen_task import *


class TestPositiveMultiExceptNumDiv2Or3(unittest.TestCase):

	def test_1_return_1(self):
		assert multi_except_num_div_2_or_3(1) == 0

	def test_11_return_385(self):
		assert multi_except_num_div_2_or_3(11) == 385


class TestNegativeMultiExceptNumDiv2Or3(unittest.TestCase):

	def test_0_return_1(self):
		assert multi_except_num_div_2_or_3(0) == 0

	def test_minus_1_return_1(self):
		assert multi_except_num_div_2_or_3(-1) == 0
