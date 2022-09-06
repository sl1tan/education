row, column = [int(i) for i in input().split()]

arr = [[int(j) for j in input().split()] for i in range(row)]

max = arr[0][0]

row_max = 0
column_max = 0

for i in range(row):
    for j in range(column):
        if arr[i][j] > max:
            max = arr[i][j]
            row_max = i
            column_max = j

print(row_max, column_max)
