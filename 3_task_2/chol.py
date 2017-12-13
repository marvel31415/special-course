import numpy as np


def Cholesky():
    N = 5
    # b = np.random.random_integers(1, 2000, size=(N, N))
    # b_symm = (b + b.T) / 2
    # print(b_symm)
    # A = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]
    # chol = np.linalg.cholesky(A)
    # print(np.linalg.det(A))
    #print(chol)
    A = np.zeros((5, 5))
    for i in range(1, 6):
        for j in range(1, 6):
            A[i-1][j-1] = 1./(i+j-1)
    print(np.linalg.cholesky(A))
    print(np.linalg.det(A))
