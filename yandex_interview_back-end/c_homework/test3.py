def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def primeDiv(a):
    for i in range(a, 0, -1):
        if a % i == 0:
            if isPrime(i):
                return i
    return 1

def gcd(a, b): 
    if b == 0: 
        return a
    else:
        return gcd(b, a % b)

def simpleDividers(n):
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
    aa = simpleDividers(a)
    bb = simpleDividers(b)
    max_prime = aa[-1] if len(aa) > 0 else 1
    min_prime = bb[-1] if len(bb) > 0 else 1

    if max_prime == min_prime:
        prev_div = primeDiv(a // max_prime)
        if gcd(a, b * prev_div) > gcd(a, b * max_prime):
            max_prime = prev_div
    else:
        max_prime = min_prime if max_prime < min_prime else max_prime

    max_b = b * max_prime
    max_a = a * max_prime

    gcd_a = gcd(a, max_b)
    gcd_b = gcd(max_a, b)
    if gcd_a > gcd_b:
        print(gcd_a)
    else:
        print(gcd_b)
