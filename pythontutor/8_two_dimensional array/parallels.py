n = int(input())

arr = [[0] * n for i in range(n)]

step = 0
for i in range(n):
    for j in range(n - 1 - step):
        arr[i][j + 1 + step] = j + 1
    step += 1

row = 0
step_2 = 0
for i in range(n):
    for j in range(row):
        arr[i][j] = row - step_2
        step_2 += 1
    step_2 = 0
    row += 1

for row in arr:
    print(" ".join(str(i) for i in row))
