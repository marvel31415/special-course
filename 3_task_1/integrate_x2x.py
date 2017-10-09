#coding=utf-8
from adaptive_integration.adaptive_integration import adaptive_integration


def integrate_x2x():
    v = lambda x: x**x
    a = 0.; b = 4
    eps = 1E-4
    result = adaptive_integration(v, a, b, eps)
    print result