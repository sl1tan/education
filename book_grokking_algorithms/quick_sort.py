def qsort2(arr):
    if len(arr) == 0:
        return arr
    if len(arr) == 1:
        return arr
    else:
        choose = arr[0]
        less = [i for i in arr[1:] if i <= choose]
        more = [i for i in arr[1:] if i > choose]
        return qsort2(less) + [choose] + qsort2(more)


def summ(arr):
    if arr == []:
        return 0
    return arr[0] + summ(arr[1:])


def len2(arr):
    if arr == []:
        return 0
    else:
        return 1 + len2(arr[1:])


def max2(arr):
    if len(arr) == 0:
        return None
    if len(arr) < 2:
        return arr[0]
    else:
        total = max2(arr[1:])
        return arr[0] if arr[0] > total else total


def binary_search(arr, x):
    begin = 0
    end = len(arr) - 1
    middle = len(arr) // 2
    while (begin <= end):
        middle = (begin + end) // 2
        if arr[middle] > x:
            end = middle - 1
        elif arr[middle] < x:
            begin = middle + 1
        elif arr[middle] == x:
            return middle
    return None


def binary(x):
    if x // 2 == 0:
        return x % 2


a = [3, 2, 10, 1, 4]
b = []
c = qsort2(a)
print(c)
print("index", binary_search(c, 4))
