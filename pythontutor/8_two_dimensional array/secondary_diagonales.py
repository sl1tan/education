n = int(input())

arr = [[0] * n for i in range(n)]

for i in range(n):
    arr[i][n - i - 1] = 1

for i in range(n):
    for j in range(n - i, n):
        arr[i][j] = 2

for row in arr:
    print(" ".join(str(i) for i in row))
