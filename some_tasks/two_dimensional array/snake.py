def Horizontal_snake(x, y):
    arr = []
    for i in range(x):
        if i % 2 == 0:
            in_arr = [i + 1 for i in range(y * i, y * (i + 1))]
            arr.append(in_arr)
        else:
            in_arr = [
                i + 1 for i in range(y * (i + 1) - 1, y * (i + 1) - 1 - y, -1)]
            arr.append(in_arr)
    return arr


n, m = [int(i) for i in input().split()]
arr = Horizontal_snake(n, m)

for row in arr:
    for elem in row:
        print("%2d " % (elem), end="")
    print()
