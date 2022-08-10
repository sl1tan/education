n = int(input())
num = 1
fib = 1
a = 0
while n != fib:
    a, fib = fib, a + fib
    num += 1
    if n == 0:
        num = 0
        break
    if fib > n:
        num = -1
        break
print(num)
