def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


for i in range(0, 5):
    print(factorial(i))


def min(*a):
    min = a[0]
    for i in range(1, len(a)):
        min = a[i] if min > a[i] else min
    return min


print(min(1, 2, 3))


def f():
    a = 1
    print(a)


a = 0
f()
print(a)


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


for i in range(1, 6):
    print(i, '! = ', factorial(i), sep='')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
