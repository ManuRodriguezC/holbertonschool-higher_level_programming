#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
from sqlite3 import threadsafety
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_doc(self):
        test = __import__('6-max_integer').max_integer
        self.assertTrue(len(test)> 1)

    def text_module(self):
        test = max_integer.__doc__
        self.assertTrue(test > 1)

    def test_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_int_negative(self):
        self.assertTrue([-2, 3, -44, 20], 20)

    def max_at_the_end(self):
        self.assertTrue(max_integer([20, 3, 22, 122]), 122)

    def max_beginning(self):
        self.assertTrue([100, 30, 40, 10], 100)

    def max_middle(self):
        self.assertTrue([10, 20 ,30, 15], 30)

    def max_only_negative(self):
        self.assertTrue([-10, -30- -5, -20], -5)

    def max_beginning(self):
        self.assertTrue([4], 4)

    def max_beginning(self):
        self.assertTrue([], None)

if __name__ == "__main__":
    unittest.main