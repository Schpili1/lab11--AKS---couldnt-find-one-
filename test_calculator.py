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
        self.assertEqual(calculator.sub(5, 3), 2)
        self.assertEqual(calculator.sub(0, 4), -4)
        self.assertEqual(calculator.sub(-2, -5), 3)

    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(-1, 5), -5)
        self.assertEqual(calculator.mul(0, 100), 0)

    def test_divide(self):
        self.assertAlmostEqual(calculator.div(2, 10), 5.0)
        self.assertAlmostEqual(calculator.div(4, -8), -2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.log(2, 8), 3.0)
        self.assertAlmostEqual(calculator.log(10, 1000), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(-2, 8)
        with self.assertRaises(ValueError):
            calculator.log(1, 10)
        with self.assertRaises(ValueError):
            calculator.log(10, 0)

    def test_exponent(self):
        self.assertEqual(calculator.exp(2, 3), 8)
        self.assertEqual(calculator.exp(5, 0), 1)
        self.assertEqual(calculator.exp(-2, 2), 4)


if __name__ == "__main__":
    unittest.main()