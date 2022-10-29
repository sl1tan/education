def output(arr):
    for row in arr:
        for elem in row:
            print("%4d" % (elem), end="")
        print()


def make_arr(n, m):
    arr = [[0] * m for i in range(n)]
    return arr


def spiral(arr):
    i = 1
    x, y = 0, 0
    rb = m
    db = n
    lb = 0
    ub = 0
    while (i < n*m - 1):
        while (y < rb):
            arr[x][y] = i
            y += 1
            i += 1
        y -= 1
        i -= 1
        rb -= 1
        while (x < db):
            arr[x][y] = i
            x += 1
            i += 1
        x -= 1
        i -= 1
        db -= 1
        while (y >= lb):
            arr[x][y] = i
            y -= 1
            i += 1
        lb += 1
        y += 1
        i -= 1
        while (x > ub):
            arr[x][y] = i
            x -= 1
            i += 1
        x += 1
        i -= 1
        ub += 1
    return arr


n, m = [int(i) for i in input().split()]
arr = make_arr(n, m)
arr = spiral(arr)

output(arr)
