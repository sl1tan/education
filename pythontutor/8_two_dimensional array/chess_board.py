row, column = [int(i) for i in input().split()]
arr = [['*'] * column for i in range(row)]

for i in range(row):
    for j in range(column):
        if i % 2 == j % 2:
            arr[i][j] = '.'

for row in arr:
    print(" ".join(row))
