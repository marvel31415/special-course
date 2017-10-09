def rectangular(f, a, b, n):
    h = (b - a) / n
    result = f(a + 0.5 * h)
    for i in range(1, n):
        result += f(a + 0.5 * h + i * h)
    result *= h
    return result