#coding=utf-8
from math import sin, pi

from adaptive_integration.adaptive_integration import adaptive_integration


def product_sines():
    a = -pi; b = pi
    eps = 1E-15
    i = 0
    for k in range(1, 11):
        for j in range(1, 11):
            v = lambda x: sin(j * x) * sin(k * x)
            print adaptive_integration(v, a, b, eps)
