import unittest
from dzen.src.dzen_task import *


class TestPositiveDoesNotEndOn3And9(unittest.TestCase):

	def test_1_return_1(self):
		assert does_not_end_on_3_and_9(1) == 1

	def test_10_return_8(self):
		assert does_not_end_on_3_and_9(10) == 8


class TestNegativeDoesNotEndOn3And9(unittest.TestCase):

	def test_minus_1_return_0(self):
		assert does_not_end_on_3_and_9(-1) == 0

	def test_0_return_0(self):
		assert does_not_end_on_3_and_9(0) == 0
