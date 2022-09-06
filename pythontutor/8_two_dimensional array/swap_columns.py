def swap_columns(arr, col_1, col_2):
    for i in range(len(arr)):
        arr[i][col_1], arr[i][col_2] = arr[i][col_2], arr[i][col_1]


row, column = [int(i) for i in input().split()]

arr = [[int(j) for j in input().split()] for i in range(row)]

col_1, col_2 = [int(i) for i in input().split()]

swap_columns(arr, col_1, col_2)

for row in arr:
    print(" ".join(str(i) for i in row))
