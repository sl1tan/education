def pascal(n, m):
    arr = [[0] * m for i in range(n)]
    for i in range(n):
        arr[i][0] = 1
    for j in range(m):
        arr[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    return arr


n, m = [int(i) for i in input().split()]
result = pascal(n, m)
for row in result:
    for i in row:
        print("%6d" % (i), end="")
    print()
