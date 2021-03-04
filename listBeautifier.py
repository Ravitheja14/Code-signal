def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        i, *res, j = res
    return res


# concept of *args
listBeautifier([3, 4, 2, 4, 38, 4, 5, 3, 2])
