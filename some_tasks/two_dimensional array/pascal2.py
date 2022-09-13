def pascal2(n):
    arr = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                arr[i].append(1)
            elif j == i:
                arr[i].append(1)
            else:
                arr[i].append(arr[i - 1][j] + arr[i - 1][j - 1])
    return arr


n = int(input())
result = pascal2(n)

for row in result:
    for i in row:
        print("%6d" % (i), end="")
    print()
