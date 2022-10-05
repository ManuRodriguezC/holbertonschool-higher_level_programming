#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_doc(self):
        test = __import__('6-max_integer').__doc__
        self.assertTrue(len(test) > 1)

    def text_module(self):
        test = max_integer.__doc__
        self.assertTrue(test > 1)

    def test_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def max_beginning(self):
        self.assertEqual(max_integer([100, 30, 40, 10]), 100)

    def max_middle(self):
        self.assertEqual(max_integer([10, 20 ,30, 15, 12]), 30)

    def test_int_negative(self):
        self.assertEqual(max_integer([2, 3, -44, 20]), 20)

    def max_only_negative(self):
        self.assertEqual(max_integer([-10, -30- -5, -20]), -5)

    def max_one_element(self):
        self.assertEqual(max_integer([4]), 8)

    def max_list_empty(self):
        self.assertIsNone(max_integer([]))

    def test_node(self):
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main