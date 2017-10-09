#coding=utf-8
from integration_methods.trapezoidal import trapezoidal


def trapezoidal_double(f, a, b, c, d, nx, ny):
    g = lambda x: trapezoidal(lambda y: f(x, y), c, d, ny)
    return trapezoidal(g, a, b, nx)
