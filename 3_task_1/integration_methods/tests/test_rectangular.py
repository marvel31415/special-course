# coding=utf-8
from integration_methods.rectangular import rectangular
from rectangular_convergence_rates import rectangular_convergence_rates


def test_rectangular_byhand():
    expected = 38
    v = lambda x: 2 * x ** 3
    computed = rectangular(v, 1., 3, 2)
    tol = 1E-15
    rel_error = abs(expected - computed)
    success = rel_error < tol
    msg = "погрешность = {0} больше допуска = {1}".format(rel_error, tol)
    assert success, msg


def test_rectangular_linear():
    v = lambda x: 2
    V = lambda x: 2 * x
    a = 1.1
    b = 2.9
    expected = V(b) - V(a)
    computed = rectangular(v, a, b, 2)
    tol = 1E-15
    rel_error = abs(expected - computed)
    success = rel_error < tol
    msg = "Погрешность: {0}".format(rel_error)
    assert success, msg


def test_rectangular_conv_rate():
    v = lambda x: 2 * x ** 3
    V = lambda x: x ** 4 / 2
    a = 1.1
    b = 2.9
    r = rectangular_convergence_rates(v, V, a, b)
    tol = 0.01
    msg = str(r[-4:])
    success = (abs(r[-1]) - 2) < tol
    assert success, msg
