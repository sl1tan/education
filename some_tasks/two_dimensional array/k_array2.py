def f(arr, k, s):
    if k > 0:
        arr = [s + "0", s + "1"]
        for i in range(2):
            arr[i] = f(arr[i], k - 1, s + str(i))
    return arr

print(f([], int(input()), ""))