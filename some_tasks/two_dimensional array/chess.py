def chess(n, m):
    arr = [[0] * m for i in range(n)]
    i = 1
    for x in range(n):
        for y in range(m):
            if x % 2 == y % 2:
                arr[x][y] = i 
                i += 1
    return arr

def output(arr):
    for row in arr:
        for elem in row:
            print("%4d"%(elem), end="")
        print()

n, m = [int(i) for i in input().split()]
arr = chess(n, m)
output(arr)