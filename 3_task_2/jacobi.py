#encoding=utf-8
import math
import time
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot


# N - размерность матрицы; A[N][N] - матрица коэффициентов, F[N] - столбец свободных членов,
# X[N] - начальное приближение, ответ записывается также в X[N];
def Jacobi (A, b, eps, N, x):
    it = 0
    TempX = zeros(N)
    while True:
        for i in range(N):
            TempX[i] = b[i]
            for g in range(N):
                if i != g:
                    TempX[i] -= A[i][g] * x[g]
            TempX[i] /= A[i][i]
        norm = math.fabs(x[0] - TempX[0])
        for h in range(N):
            if math.fabs(x[h] - TempX[h]) > norm:
                norm = math.fabs(x[h] - TempX[h])
            x[h] = TempX[h]
        it += 1
        if norm < eps:
            break
    return x, it


if __name__ == '__main__':

    start_time = time.time()

    eps = 0.001  # желаемая точность
    A = array([[2.0, 1.0], [5.0, 7.0]])
    b = array([11.0, 13.0])
    guess = array([1.0, 1.0])

    sol, iterations = Jacobi(A, b, eps, N=2, x=guess)
    print "A:"
    pprint(A)

    print "b:"
    pprint(b)

    print "x:"
    pprint(sol)
    print("--- {} seconds ---".format(time.time() - start_time))
    print "number of iterations is {0}".format(iterations)
