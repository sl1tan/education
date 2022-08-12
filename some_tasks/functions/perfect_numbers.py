def divs(n):
    enum = []
    for i in range(1, n):
        if n % i == 0:
            enum.append(i)
    return enum


def sum(a):
    sum = 0
    for elem in a:
        sum += elem
    return sum


def isPerfect(n):
    summ = sum(divs(n))
    return summ == n


for i in range(50):
    print(i, isPerfect(i))

print(496, isPerfect(496))
