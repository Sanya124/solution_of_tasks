import unittest
from geekbrains.src.geekbrains_task import multi_of_list_items


class TestPositiveMultiOfListItems(unittest.TestCase):

    def test_3_return_int(self):
        assert type(multi_of_list_items(3)) == int

    def test_4_return_int(self):
        assert type(multi_of_list_items(4)) == int
