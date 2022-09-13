def IsSymmetric(arr):
    flag = 1
    step = 0
    for row in range(n - 1):
        for column in range(1 + step, n):
            if arr[row][column] != arr[column][row]:
                return "NO"
        step += 1
    if flag:
        return "YES"


n = int(input())

arr = [[int(j) for j in input().split()] for i in range(n)]
print(IsSymmetric(arr))

# for row in arr:
#     print(" ".join([str(i) for i in row]))
