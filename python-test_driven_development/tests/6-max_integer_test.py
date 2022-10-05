#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

class TestMaxInteger(unittest.TestCase):

    def test_int(self):
        self.assertTrue([1, 2, 3, 4], 4)

    def test_int_negative(self):
        self.assertTrue([-2, 3, -44, 20], 20)

if __name__ == "__main__":
    unittest.main