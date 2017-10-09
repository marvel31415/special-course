# coding=utf-8
from integration_methods.rectangular import rectangular


def left_rectangular_method(f, a, b, n):
    h = (b - a) / n
    result = f(a)
    for i in range(1, n):
        result += f(a + h * i)
    result *= h
    return result


def right_rectangular_method(f, a, b, n):
    h = (b - a) / n
    result = f(a + h)
    for i in range(2, n+1):
        result += f(a + h * i)
    result *= h
    return result


def rectangular_methods(f, a, b, n, rec):
    if rec == 'right':
        return right_rectangular_method(f, a, b, n)
    elif rec == 'left':
        return left_rectangular_method(f, a, b, n)
    elif rec == 'mid':
        return rectangular(f, a, b, n)
