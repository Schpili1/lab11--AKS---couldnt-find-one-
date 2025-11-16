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


def sub(a, b):
    return a - b


def subtract(a, b):
    return sub(a, b)


def mul(a, b):
    return a * b


def multiply(a, b):
    return mul(a, b)


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero when a == 0.")
    return b / a


def divide(a, b):
    return div(a, b)


def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid values for logarithm.")
    return math.log(b, a)


def logarithm(a, b):
    return log(a, b)


def exp(a, b):
    return a ** b


def exponent(a, b):
    return exp(a, b)