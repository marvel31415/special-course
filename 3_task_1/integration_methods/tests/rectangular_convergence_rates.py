from math import log

from numpy import zeros

from integration_methods.rectangular import rectangular


def rectangular_convergence_rates(f, F, a, b, num_expected = 14):
    expected = F(b) - F(a)
    n = zeros(num_expected, dtype = int)
    E = zeros(num_expected)
    r = zeros(num_expected)
    for i in range(num_expected):
        n[i] = 2**(i+1)
        computed = rectangular(f, a, b, n[i])
        E[i] = abs((expected - computed)/expected)
        if i > 0:
            r_im1 = log(E[i]/E[i-1])/log(float(n[i]/n[i-1]))
            r[i-1] = float('%.2f' % r_im1)
    return r