def mult(n, m):
    arr = [[int(i * j) for j in range(m)] for i in range(n)]
    return arr

def output(arr):
    for row in arr:
        for elem in row:
            print("%4d"%(elem), end="")
        print()

n, m = [int(i) for i in input().split()]
arr = mult(n , m)
output(arr)