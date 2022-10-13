def count_negative(arr):
    if arr == []:
        return 0
    else:
        return 1 * (arr[0] < 0) + count_negative(arr[1:])


def sum_in(arr):
    summ = 0
    for i in arr:
        if not isinstance(i, list):
            summ += i
        else:
            summ += sum_in(i)
    return summ

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def power(x, pow):
    if pow == 1:
        return x
    else:
        return x * power(x, pow - 1)

def binary(x):
    if x // 2 == 0:
        return str(x % 2)
    else:
        return binary(x//2) + str(x % 2)



arr = [0, -2, -3, 111]
arr2 = [[0, 1, 2], 3, [4, 5, 6]]
print(count_negative(arr))
print(sum_in(arr2))
print(fibonacci(10))
print(power(2, 10))
print(binary(126))