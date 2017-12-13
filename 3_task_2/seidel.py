from numpy import dot, zeros_like, allclose, array
import time

def Seidel(A, b, it_limit):
    x = zeros_like(b)
    it = 0
    for it_count in range(1, it_limit):
        x_new = zeros_like(x)
        for i in range(A.shape[0]):
            s1 = dot(A[i, :i], x_new[:i])
            s2 = dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
            it = it_count
        if allclose(x, x_new, rtol=1e-3):
            it = it_count
            break
        x = x_new
    return x, it


if __name__ == '__main__':

    start_time = time.time()
    A = array([[ 2., -3.,  0.,  0.,  0.],
       [ 1.,  2., -3.,  0.,  0.],
       [ 0.,  1.,  2., -3.,  0.],
       [ 0.,  0.,  1.,  2., -3.],
       [ 0.,  0.,  0.,  1.,  2.]])
    # initialize the RHS vector
    b = array([-1.,  0.,  0.,  0.,  3.])

    #print("System of equations:")
    #for i in range(A.shape[0]):
    #     row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    #     print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))
    x, iterations = Seidel(A, b, 1000)
    print("Solution: {0}".format(x))
    error = dot(A, x) - b
    print("Error: {0}".format(error))
    print "Iterations number is {}".format(iterations)
    print("--- {} seconds ---".format(time.time() - start_time))
