# https://github.com/Schpili1/lab11--AKS---couldnt-find-one-
# Partner 1: Alexander Schpilberg
# Partner 2: (Worked alone)

import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero when a == 0.")
    return b / a


def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid values for logarithm.")
    return math.log(b, a)


def exp(a, b):
    return a ** b