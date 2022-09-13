def diagonal(arr, k):
    row, column = 0, 0
    if k > 0:
        row += abs(k)
    elif k < 0:
        column += abs(k)

    res = []
    for n in range(len(arr) - abs(k)):
        res.append(arr[row][column])
        row += 1
        column += 1

    print(" ".join([str(i) for i in res]))


n = int(input())

arr = [[int(j) for j in input().split()] for i in range(n)]

k = int(input())

diagonal(arr, k)
