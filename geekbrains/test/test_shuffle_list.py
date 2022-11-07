import unittest
from geekbrains.src.geekbrains_task import shuffle_list


class TestPositiveMultiOfListItems(unittest.TestCase):

    def test_shuffle(self):
        test_list = [1, 2]
        shuffled = shuffle_list(test_list)
        assert shuffled != test_list
