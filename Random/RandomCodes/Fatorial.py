def F(n):
    fat = 1
    while n > 1:
        fat = n * fat
        n = n - 1
    return fat