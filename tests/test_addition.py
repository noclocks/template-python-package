"""Unit Tests for Addition Module"""

import unittest

from pkg.addition import add_one, add_n 


class TestAddition(unittest.TestCase):

    def test_add_one(self):
      self.assertEqual(add_one(5), 6)

  
    def test_add_n(self):
        self.assertEqual(add_n(5, 1), 6)


if __name__ == '__main__':
    unittest.main()
