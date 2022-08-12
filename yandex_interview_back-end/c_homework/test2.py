import math


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def divs(n):
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return result


def maxPrime(a):
    for i in range(len(a) - 1, 0, -1):
        if isPrime(a[i]):
            return a[i]
    return 1


count = int(input())
nums = []
for i in range(count):
    a, b = [int(i) for i in input().split()]
    nums.append(a)
    nums.append(b)

for i in range(0, len(nums), 2):
    a, b = nums[i], nums[i + 1]
    if a < b:
        a, b = b, a
    max_divs = divs(a)
    min_divs = divs(b)
    max_prime = maxPrime(max_divs)
    min_prime = maxPrime(min_divs)
    max_prime = min_prime if max_prime < min_prime else max_prime
    b *= max_prime
    max_gcd = math.gcd(a, b)
    print(max_gcd)
