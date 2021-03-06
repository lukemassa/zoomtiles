
import unittest
import rectangle
import square
from fractions import Fraction


class TestSquare(unittest.TestCase):

    def test_get_next_perfect_square(self):

        def test_one(n, expected_next_perfect_square):
            actual_next_perfect_square = square.get_next_perfect_square(n)
            self.assertEqual(actual_next_perfect_square, expected_next_perfect_square)

        test_one(1, 1)
        test_one(2, 4)
        test_one(4, 4)
        test_one(8, 9)
        test_one(10, 16)
        test_one(99, 100)
        test_one(100, 100)
        test_one(101, 121)


    def test_results_same(self):

        def test_one(n):
            s = rectangle.Rectangle(Fraction(1, 1))
            self.assertEqual(s.solve(n), square.solve(n))

        test_one(1)
        test_one(2)
        test_one(4)
        test_one(9)
        test_one(12)
        test_one(1000)
        test_one(1001)
        test_one(203980918)
