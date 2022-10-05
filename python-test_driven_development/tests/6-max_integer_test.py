#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test with unittest a max_integer function"""
    def test_doc(self):
        test = __import__('6-max_integer').__doc__
        self.assertTrue(len(test) > 1)

    def text_module(self):
        test = max_integer.__doc__
        self.assertTrue(test > 1)

    def test_int(self):
        lists = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(lists), 5)

    def max_beginning(self):
        lists = [80, 70, 60, 50, 40]
        self.assertEqual(max_integer(lists), 80)

    def max_middle(self):
        lists = [10, 20, 30, 15, 12]
        self.assertEqual(max_integer(lists), 30)

    def test_int_negative(self):
        lists = [2, 3, -44, 20, 10]
        self.assertEqual(max_integer(lists), 20)

    def max_only_negative(self):
        lists = [-10, -30- -5, -20, -23]
        self.assertEqual(max_integer(lists), -5)

    def max_one_element(self):
        lists = [4]
        self.assertEqual(max_integer(lists), 4)

    def max_list_empty(self):
        lists = []
        self.assertIsNone(max_integer(lists))

    def test_node(self):
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main