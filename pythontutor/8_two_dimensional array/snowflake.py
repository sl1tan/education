n = int(input())

arr = []

for i in range(n):
    arr.append(['.'] * n)

for i in range(n):
    arr[n // 2][i] = '*'
    arr[i][n // 2] = '*'
    arr[i][i] = '*'
    arr[i][n - i - 1] = '*'

for row in arr:
    print(" ".join(row))
