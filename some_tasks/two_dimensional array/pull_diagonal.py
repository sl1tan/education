def pull(n, m):
    arr = [[0] * m for i in range(n)]
    amount_diagonals = m + n - 1
    c = 1
    for i in range(amount_diagonals):
        for j in range(n):
            if ((i-j) >= 0) and ((i-j) < m):
                arr[j][i-j]+=c
                c+=1
    return arr

n, m = [int(i) for i in input().split()]

arr = pull(n, m)

for row in arr:
    for elem in row:
        print("%4d"%(elem), end="")
    print()