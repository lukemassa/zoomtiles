
import unittest
import rectangle
from fractions import Fraction


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.square = rectangle.Rectangle(Fraction(1, 1))
    def test_possible_dimensions(self):

        def test_one(n, expected_dimensions):
            result = list(self.square.possible_dimensions(n))
            self.assertEqual(result, expected_dimensions)

        test_one(0, [])
        test_one(1, [(1,1)])
        test_one(2, [(1,2)])
        test_one(4, [(1,4), (2, 2)])
        test_one(7, [(1,7), (2, 4), (3, 3)])
        test_one(9, [(1,9), (2, 5), (3, 3)])

    def test_get_efficiency(self):

        def test_one(n, x, y, expected_efficiency):
            actual_efficiency = self.square.get_efficiency(n, x, y)
            self.assertEqual(actual_efficiency, expected_efficiency)

        test_one(1, 1, 1, 1)
        with self.assertRaises(AssertionError):
            test_one(2, 1, 1, 1)
        test_one(1, 2, 2, .25)
        test_one(3, 2, 2, .75)
        test_one(4, 2, 2, 1)
        test_one(2, 2, 4, .125)

    def test_solve(self):

        def test_one(n, expected_range, strict=False):
            actual_solved = self.square.solve(n)
            if strict:
                self.assertLess(expected_range[0], actual_solved)
                self.assertLess(actual_solved, expected_range[1])
            else:
                self.assertLessEqual(expected_range[0], actual_solved)
                self.assertLessEqual(actual_solved, expected_range[1])

        # Perfect squares are perfectly efficient
        test_one(1, (1, 1))
        test_one(9, (1, 1))

        # Two is the worst at 50%
        test_one(2, (.5, .5))

        # Other random ones should all be strictly between .5 and 1
        test_one(3, (.5, 1))
        test_one(101, (.5, 1))
        test_one(109548, (.5, 1))
