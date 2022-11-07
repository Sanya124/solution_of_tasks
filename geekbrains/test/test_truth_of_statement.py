import unittest
from geekbrains.src.geekbrains_task import truth_of_statement


class TestTruthOfStatement(unittest.TestCase):

    def test_return_list(self):
        assert type(truth_of_statement()) == list
