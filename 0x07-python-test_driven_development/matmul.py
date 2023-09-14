def mat(a, b):
    i = len(a)
    j = len(a[0])
    k = len(b)

    for o in range(i):
        for p in range(j):
            s = 0
            for m in range(k):
                s += a[o][m] * b[m][p]
            print(s, " ")
mat([[1,2],[1, 2]], [[1, 3],[1, 3]])

