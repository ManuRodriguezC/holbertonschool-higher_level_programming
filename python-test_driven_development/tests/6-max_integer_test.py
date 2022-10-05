#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

class TestMaxInteger(unittest.TestCase):

    def test_int(self):
        self.assertTrue([1, 2, 3, 4], 4)

    def test_int_negative(self):
        self.assertTrue([-2, 3, -44, 20], 20)

    def max_at_the_end(self):
        self.assertTrue([20, 3, 22, 122], 122)

if __name__ == "__main__":
    unittest.main