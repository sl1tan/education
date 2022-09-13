def Transpose(arr):
    n = len(arr)
    m = len(arr[0])
    res = [[0] * n for i in range(m)]
    for j in range(m):
        for i in range(n):
            res[j][i] = arr[i][j]
    return res


n, m = [int(i) for i in input().split()]

arr = [[int(j) for j in input().split()] for i in range(n)]

trans = Transpose(arr)

print("===================================")
for row in trans:
    print(" ".join([str(i) for i in row]))
