#coding=utf-8
from adaptive_integration.adaptive_integration import adaptive_integration


def test_adaptive_integration():
    v = [lambda x: x**2, lambda x: x **(1./2)]
    a = 0.; b = 2
    epss = [1E-1, 1E-10]
    for f in v:
        for eps in epss:
            adaptive_integration(f, a, b, eps)
