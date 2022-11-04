import unittest
from dzen.src.dzen_task import *


class TestPositiveMinNatNum(unittest.TestCase):

	def test_1_return_56(self):
		assert min_nat_num(1) == 56

	def test_9_return_504(self):
		assert min_nat_num(9) == 504


class TestNegativeMinNatNum(unittest.TestCase):

	def test_minus_1_return_except(self):
		assert min_nat_num(0) == 'Необходимо вводить целочисленное число от 1 до бесконечности'

	def test_0_return_except(self):
		assert min_nat_num(0) == 'Необходимо вводить целочисленное число от 1 до бесконечности'
