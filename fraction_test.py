import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())


    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        # 41/20 = 4/5 + 5/4
        self.assertEqual(Fraction(41, 20), Fraction(4, 5) + Fraction(5, 4))
        # 3/4 = 1/4 + 2/4
        self.assertEqual(Fraction(3, 4), Fraction(1, 4) + Fraction(2, 4))
        # 16/15 = 2/3 + 2/5
        self.assertEqual(Fraction(16, 15), Fraction(2, 3) + Fraction(2, 5))
        # 1/1 = 4/8 + 1/2
        self.assertEqual(Fraction(1, 1), Fraction(4, 8) + Fraction(1, 2))
        # 7/24 = 1/8 + 1/6
        self.assertEqual(Fraction(7, 24), Fraction(1, 8) + Fraction(1, 6))

    def test_sub(self):
        # -1/3 = 1/6 - 1/2
        self.assertEqual(Fraction(-1, 3), Fraction(1, 6) - Fraction(1, 2))
        # 1/2 = 1/1 - 1/2
        self.assertEqual(Fraction(1, 2), Fraction(1, 1) - Fraction(1, 2))
        # -1/4 = 1/4 - 2/4
        self.assertEqual(Fraction(-1, 4), Fraction(1, 4) - Fraction(2, 4))
        # -4/15 = 2/5 - 2/3
        self.assertEqual(Fraction(-4, 15), Fraction(2, 5) - Fraction(2, 3))
        # 10/8 = 3/2 - 2/8
        self.assertEqual(Fraction(10, 8), Fraction(3, 2) - Fraction(2, 8))
        # 5/12 = 3/4 - 1/3
        self.assertEqual(Fraction(5, 12), Fraction(3, 4) - Fraction(1, 3))

    def test_mul(self):
        # 1/18 = 1/12 * 2/3
        self.assertEqual(Fraction(1, 18), Fraction(1, 12) * Fraction(2, 3))
        # 1/4 = 3/4 * 1/3
        self.assertEqual(Fraction(1, 4), Fraction(3, 4) * Fraction(1, 3))
        # 1/2 = 1/1 * 1/2
        self.assertEqual(Fraction(1, 2), Fraction(1, 1) * Fraction(1, 2))
        # 4/15 = 2/3 * 2/5
        self.assertEqual(Fraction(4, 15), Fraction(2, 3) * Fraction(2, 5))
        # 1/8 = 1/4 * 2/4
        self.assertEqual(Fraction(1, 8), Fraction(1, 4) * Fraction(2, 4))
        # 3/16 = 1/8 * 3/2
        self.assertEqual(Fraction(3, 16), Fraction(1, 8) * Fraction(3, 2))

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        #TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0

        f = Fraction(2, 0)
        g = Fraction(1, 0)
        h = Fraction(-1, 0)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))

        f = Fraction(3, 5)
        g = Fraction(9, 15)
        h = Fraction(27, 44)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))

        f = Fraction(-1, 2)
        g = Fraction(-2, 4)
        h = Fraction(-2, 8)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))

        f = Fraction(-3, 4)
        g = Fraction(-18, 24)
        h = Fraction(-6, 24)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))


if __name__ == '__main__':
     unittest.main(verbosity=2)
