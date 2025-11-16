# https://github.com/Schpili1/lab11--AKS---couldnt-find-one-
# Partner 1: Alexander Schpilberg
# Partner 2: (Worked alone)

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(0, 4), -4)
        self.assertEqual(calculator.subtract(-2, -5), 3)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-1, 5), -5)
        self.assertEqual(calculator.multiply(0, 100), 0)

    def test_divide(self):
        # divide(a, b) returns b / a
        self.assertAlmostEqual(calculator.divide(2, 10), 5.0)
        self.assertAlmostEqual(calculator.divide(4, -8), -2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)
        self.assertAlmostEqual(calculator.logarithm(10, 1000), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(0, 0), 0.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(0), 0.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)


if __name__ == "__main__":
    unittest.main()