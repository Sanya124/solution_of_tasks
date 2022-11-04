import unittest
from dzen.src.dzen_task import *


class TestPositiveNotContains(unittest.TestCase):

	def test_33_return_18(self):
		assert not_contains_3(33) == 18


class TestNegativeNotContains(unittest.TestCase):

	def test_minus_1_return_except(self):
		answer = 'Необходимо ввести двузначное число'
		assert not_contains_3(-1) == answer

	def test_9_return_except(self):
		answer = 'Необходимо ввести двузначное число'
		assert not_contains_3(3) == answer

	def test_100_return_except(self):
		answer = 'Необходимо ввести двузначное число'
		assert not_contains_3(100) == answer
