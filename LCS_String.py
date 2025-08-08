def fn(x,y):
    m,n = len(x),len(y)
    d = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j - 1]: d[i][j] = d[i-1][j-1] + 1
            else: d[i][j] = max(d[i-1][j],d[i][j-1])
    return d[m][n]

x  = "ABCDE"
y = "BDCADE"
print(fn(x,y))