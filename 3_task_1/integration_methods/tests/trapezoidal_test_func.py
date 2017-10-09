from integration_methods.rectangular import rectangular
from integration_methods.trapezoidal import trapezoidal


def trapezoidal_test_func():
    exact = 44
    v = lambda x: 2*x**3
    n = 2
    numerical = trapezoidal(v, 1., 3, n)
    error = abs(exact - numerical)
    print ('error: ', error)

def rectangular_test_func():
    exact = 33.5
    v = lambda x: 2 * x ** 3
    n = 2
    numerical = rectangular(v, 1., 3, n)
    error = abs(exact - numerical)
    print ('error: ', error)