# coding=utf-8
from math import sqrt

from integration_methods.rectangular_methods import rectangular_methods
from rectangular_methods_convergence_rates import rectangular_methods_convergence_rates


def test_rectangular_methods_byhand():
    rec = ['left', 'right', 'mid']
    expected = [3.716924933646271, 6.383591600312938, 5.4086026688685]
    v = lambda x: sqrt(x)
    for i in range(len(rec)):
        computed = rectangular_methods(v, 0., 4, 3, rec[i])
        tol = 1E-14
        rel_error = abs(computed - expected[i])
        success = rel_error < tol
        msg = "погрешность = {0} больше допуска = {1}".format(rel_error, tol)
        assert success, msg


def test_rectangular_methods_linear():
    v = lambda x: 2
    V = lambda x: 2 * x
    a = 1.; b = 3
    expected = V(b) - V(a)
    rec = ['left', 'right', 'mid']
    for i in range(len(rec)):
        computed = rectangular_methods(v, a, b, 3, rec[i])
        tol = 1E-15
        rel_error = abs(computed - expected)
        success = rel_error < tol
        msg = "Погрешность: {0}".format(rel_error)
        assert success, msg


def test_rectangular_methods_conv_rates():
    v = lambda x: 2
    V = lambda x: 2 * x
    a = 1; b = 3
    rec = ['left', 'right', 'mid']
    for i in range(len(rec)):
        r = rectangular_methods_convergence_rates(v, V, a, b, rec[i])
        tol = 0.01
        msg = str(r[-4:])
        success = (abs(r[-1]) - 2) < tol
        assert success, msg
