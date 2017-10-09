from integration_methods.rectangular import rectangular
from integration_methods.trapezoidal import trapezoidal


def integrate_parabola():
    v = lambda x: x*(x-1)
    n_1 = 2
    n_2 = 100
    tr_1 = trapezoidal(v, 2., 6, n_1)
    rec_1 = rectangular(v, 2., 6, n_1)
    tr_2 = trapezoidal(v, 2., 6, n_2)
    rec_2 = rectangular(v, 2., 6, n_2)
    error_2 = tr_1 - rec_1
    error_100 = tr_2 - tr_1
    print ("error for 2 breaks: ", error_2)
    print ("error for 100 breaks", error_100)
