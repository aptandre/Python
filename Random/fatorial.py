def f(n):
    v = n - 1
    while v > 1:
        n = n * v
        v = v - 1
    return n