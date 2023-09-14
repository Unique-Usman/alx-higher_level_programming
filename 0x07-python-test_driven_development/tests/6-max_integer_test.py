#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """function for testing max integer"""

    def test_max_end(self):
        """test max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_begin(self):
        """test max in the at the begin"""
        self.assertEqual(max_integer([4, 2, 3, 4]), 4)

    def test_max_middle(self):
        """test max in the at the begin"""
        self.assertEqual(max_integer([1, 1, 4, 3, 2]), 4)

    def test_max_contain_negative(self):
        """test max in the at the begin"""
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_all_negative(self):
        """test max in the at the begin"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_contain_one_ele(self):
        """test max in the at the begin"""
        self.assertEqual(max_integer([4]), 4)

    def test_max_empty(self):
        """test max in the at the begin"""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
