def sum(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum


def mult(a):
    mult = 1
    for i in range(len(a)):
        mult *= a[i]
    return mult


print(sum([1, 2, 3, 4]))
print(mult([8, 2, 3, -1, 7]))
