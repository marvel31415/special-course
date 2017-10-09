# coding=utf-8
from integration_methods.trapezoidal import trapezoidal


def adaptive_integration(f, a, b, eps, method='trapezoidal'):
    n = 1
    while abs(trapezoidal(f, a, b, n) - trapezoidal(f, a, b, 2 * n)) >= eps:
        n *= 2
    result = trapezoidal(f, a, b, 2 * n)
    print abs(result - trapezoidal(f, a, b, n))
    return result
