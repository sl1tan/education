def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


print(isPrime(1))
print(isPrime(2))
print(isPrime(3))
print(isPrime(10))
