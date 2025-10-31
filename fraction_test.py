import unittest
from main import Fraction


class TestFraction(unittest.TestCase):
    def test_reduce_on_creation(self):
        cases = [(4, 6, 2, 3), (10, 5, 2, 1), (-8, 4, -2, 1), (3, -9, -1, 3), (-6, -3, 2, 1)]

        for num, den, exp_num, exp_den in cases:
            frac = Fraction(num, den)
            self.assertEqual(frac.numerator, exp_num)
            self.assertEqual(frac.denominator, exp_den)

    def test_zero_denominator_raises(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_not_number_raises(self):
        with self.assertRaises(TypeError):
            Fraction("1", "a")

    def test_add_fraction(self):
        cases = [
            (Fraction(0, 7), Fraction(3, 19), 3, 19),
            (Fraction(9, 7), Fraction(3, 19), 192, 133),
            (Fraction(-3, 7), Fraction(4, 3), 19, 21),
            (Fraction(0, 12), Fraction(0, 21), 0, 1),
            (Fraction(-39, 7), Fraction(4, 3), -89, 21),
        ]

        for left, right, exp_num, exp_den in cases:
            frac = left + right
            self.assertEqual(frac.numerator, exp_num)
            self.assertEqual(frac.denominator, exp_den)

    def test_sub_fraction(self):
        cases = [
            (Fraction(0, 7), Fraction(9, 75), -3, 25),
            (Fraction(51, 14), Fraction(7, 2), 1, 7),
            (Fraction(-65, -2), Fraction(-9, -7), 437, 14),
            (Fraction(1, -111), Fraction(2, -222), 0, 1)
        ]

        for left, right, exp_num, exp_den in cases:
            frac = left - right
            self.assertEqual(frac.numerator, exp_num)
            self.assertEqual(frac.denominator, exp_den)

    def test_multiplication_by_fraction(self):
        cases = [
            (Fraction(0, 7), Fraction(4, 3), 0, 1),
            (Fraction(9, 7), Fraction(4, 3), 12, 7),
            (Fraction(-2, 7), Fraction(4, 3), -8, 21),
            (Fraction(-2, 7), Fraction(-2, 3), 4, 21),
        ]

        for left, right, exp_num, exp_den in cases:
            frac = left * right
            self.assertEqual(frac.numerator, exp_num)
            self.assertEqual(frac.denominator, exp_den)

    def test_division_by_fraction(self):
        cases = [
            (Fraction(5, 13), Fraction(7, 6), 30, 91),
            (Fraction(10, 25), Fraction(2, 15), 3, 1),
            (Fraction(36, 521), Fraction(45, 35), 28, 521),
            (Fraction(1, 1), Fraction(1, 1), 1, 1),
            (Fraction(0, 12), Fraction(12, 12), 0, 1),
        ]

        for left, right, exp_num, exp_den in cases:
            frac = left / right
            self.assertEqual(frac.numerator, exp_num)
            self.assertEqual(frac.denominator, exp_den)
