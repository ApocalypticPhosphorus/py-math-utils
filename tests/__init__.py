import unittest
import sys
import os

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from math_utils.core import almost_equal_tolerance

class TestCoreMath(unittest.TestCase):
    def test_exact_match(self):
        self.assertTrue(almost_equal_tolerance(5.0, 5.0, 0.01))

    def test_within_tolerance(self):
        self.assertTrue(almost_equal_tolerance(5.0, 5.005, 0.01))
        self.assertTrue(almost_equal_tolerance(5.0, 4.995, 0.01))

    def test_outside_tolerance(self):
        self.assertFalse(almost_equal_tolerance(5.0, 5.02, 0.01))
        self.assertFalse(almost_equal_tolerance(5.0, 4.98, 0.01))

    def test_negative_numbers(self):
        self.assertTrue(almost_equal_tolerance(-5.0, -5.005, 0.01))
        self.assertFalse(almost_equal_tolerance(-5.0, -5.02, 0.01))

    def test_mixed_signs(self):
        self.assertTrue(almost_equal_tolerance(5.0, -5.0, 10))
        self.assertTrue(almost_equal_tolerance(5.0, -5.0, 10.1))
        self.assertFalse(almost_equal_tolerance(5.0, -5.0, 9.99)) 

    def test_zero_tolerance(self):
        self.assertTrue(almost_equal_tolerance(5.0, 5.0, 0))
        self.assertFalse(almost_equal_tolerance(5.0, 5.0001, 0))

    def test_large_numbers(self):
        self.assertTrue(almost_equal_tolerance(1e9, 1e9 + 5, 10))
        self.assertFalse(almost_equal_tolerance(1e9, 1e9 + 15, 10))

    #def test_gcd(self):
    #    self.assertEqual(gcd(48, 18), 6)
    #    self.assertEqual(gcd(101, 103), 1)

if __name__ == '__main__':
    unittest.main()