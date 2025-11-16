"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# https://github.com/Schpili1/lab11--AKS---couldnt-find-one-
# Partner 1: Alexander Schpilberg
# Partner 2: (Worked alone)

import math


def square_root(a):
    if a < 0:
        raise ValueError("square_root() undefined for negative numbers.")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero when a == 0.")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid values for logarithm.")
    return math.log(b, a)


def exponent(a, b):
    return a ** b