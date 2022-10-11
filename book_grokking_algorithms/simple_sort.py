def find_small(arr):
    small = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < small:
            small = arr[i]
            index = i
    return index

def sort(arr):
    new_arr = []
    for x in range(len(arr)):
        index = find_small(arr)
        new_arr.append(arr.pop(index))
    return new_arr

A = [3, 1, 5, 7, 8, 8, 100, 99]
print(sort(A))