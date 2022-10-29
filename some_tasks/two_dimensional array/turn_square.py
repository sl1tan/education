def output(arr):
    for row in arr:
        for elem in row:
            print("%4d" % (elem), end="")
        print()


def turn(arr, n, m):
    new_arr = [[0] * n for x in range(m)]
    for y in range(m):
        for x in range(n - 1, -1, -1):
            new_arr[y][x] = arr[n - x - 1][y]
    return new_arr


n = int(input())
arr = [[int(i) for i in input().split()] for x in range(n)]
new_arr = turn(arr, n, n)
output(new_arr)
