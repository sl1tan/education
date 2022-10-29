def f(arr, k):
    if k > 0:
        arr = [0] * 2
        for i in range(2):
            arr[i] = f(arr[i], k - 1)
    return arr


k = int(input())

print(f([], k))
