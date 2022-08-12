def power(a, n):
    res = 1
    if n > 0:
        res *= a * power(a, n - 1)
    return res


a = float(input())
n = int(input())

print(power(a, n))
