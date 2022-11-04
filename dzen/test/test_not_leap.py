import unittest
from dzen.src.dzen_task import *


class Test(unittest.TestCase):

	def test_not_leap(self):
		assert not_leap() == 1515
