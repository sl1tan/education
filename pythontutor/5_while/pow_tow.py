n = int(input())
pow = 1
i = 0
while pow * 2 <= n:
    pow *= 2
    i += 1
print(i, pow)
