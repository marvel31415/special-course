#coding=utf-8
import sympy

from double_integration.trapezoidal_double import trapezoidal_double


def test_trapezoidal_double_byhand():
    f = lambda x, y: 2 * x + y
    a = 0
    b = 2
    c = 2
    d = 3
    x, y = sympy.symbols('x y')
    I_expected = sympy.integrate(f(x, y), (x, a, b), (y, c, d))
    for nx, ny in (3, 5), (4, 4), (5, 3):
        I_computed1 = trapezoidal_double(f, a, b, c, d, nx, ny)
        tol = 1E-14
        assert abs((I_computed1 - I_expected) / I_expected) < tol
