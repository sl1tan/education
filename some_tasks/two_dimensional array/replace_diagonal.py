def SwapDiagonals(arr):
    res = [row[:] for row in arr]
    n = len(res)
    for i in range(n):
        res[i][i], res[n - 1 - i][i] = res[n - 1 - i][i], res[i][i]
    return res


n = int(input())
arr = [[int(j) for j in input().split()] for i in range(n)]
result = SwapDiagonals(arr)
print("======================================")
for row in result:
    print(" ".join([str(i) for i in row]))
