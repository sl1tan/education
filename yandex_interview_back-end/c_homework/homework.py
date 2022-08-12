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


def primeDivs(a):
    for i in range(a, 0, -1):
        if isPrime(i):
            return i


def issimple(n):
    answer = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            answer.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        answer.append(n)
    return answer


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
    max_divs = issimple(a)
    min_divs = issimple(b)
    max_divs.insert(0, 1)
    min_divs.insert(0, 1)
    max_prime = max(max_divs)
    min_prime = max(min_divs)
    max_prime = min_prime if max_prime < min_prime else max_prime
    max_a = a * max_prime
    max_b = b * max_prime
    a_gcd = math.gcd(max_a, b)
    b_gcd = math.gcd(a, max_b)
    if a_gcd > b_gcd:
        print(a_gcd)
    else:
        print(b_gcd)
