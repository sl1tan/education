def output(arr):
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[0]) - 1):
            print("{:2}".format(arr[i][j]), end="")
        print()


def make_arr(n, m):
    arr = [["0"] * m for i in range(n)]
    return arr


def sapper(arr):
    for x in range(1, len(arr) - 1):
        for y in range(1, len(arr[0]) - 1):
            count = 0
            if arr[x][y] != "*":
                if arr[x][y + 1] == "*":
                    count += 1
                if arr[x][y - 1] == "*":
                    count += 1
                if arr[x + 1][y] == "*":
                    count += 1
                if arr[x - 1][y] == "*":
                    count += 1
                if arr[x + 1][y - 1] == "*":
                    count += 1
                if arr[x + 1][y + 1] == "*":
                    count += 1
                if arr[x - 1][y - 1] == "*":
                    count += 1
                if arr[x - 1][y + 1] == "*":
                    count += 1
                arr[x][y] = str(count)
    return arr


n, m, mines = [int(i) for i in input().split()]
arr = make_arr(n + 2, m + 2)

for i in range(mines):
    x, y = [int(i) for i in input().split()]
    arr[x][y] = "*"

output(sapper(arr))
